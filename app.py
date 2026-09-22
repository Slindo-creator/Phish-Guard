import os
import sys
import pickle
import sqlite3
from flask import Flask, render_template, request, redirect, url_for

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import log_incident, get_all_logs, init_db

def check_whitelist_locally(url):
    """Queries the phishguard.db directly to check if a domain is whitelisted."""
    try:
        conn = sqlite3.connect("phishguard.db")
        cursor = conn.cursor()
        cursor.execute("SELECT domain FROM whitelist")
        domains = cursor.fetchall()
        conn.close()
        
        for row in domains:
            domain_str = row[0]
            if domain_str in url.lower():
                return True
    except Exception as e:
        print(f"Whitelist database lookup skipped: {e}")
    return False

def url_tokenizer(url):
    return url.split('/')

app = Flask(__name__)

if not os.path.exists("phishguard.db"):
    init_db()

try:
    with open('phishing_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)
    print("AI Model and Vectorizer loaded successfully!")
except Exception as e:
    print(f" Error loading AI files: {e}. Please run model.py first.")

@app.route('/')
def dashboard():
    logs = get_all_logs()
    return render_template('dashboard.html', logs=logs)

@app.route('/scan', methods=['POST'])
def scan_url():
    input_url = request.form.get('url', '').strip()
    
    if not input_url:
        return redirect(url_for('dashboard'))

    if check_whitelist_locally(input_url):
        risk_score = 0.00
        status = "SAFE"
        action_taken = "Whitelisted Domain (Connection Allowed)"
        
    if check_whitelist_locally(input_url):
        risk_score = 0.00
        payment_safety = "Whitelisted Domain"
        is_payment_page = False
    else:
        vectorized_url = vectorizer.transform([input_url])
        probabilities = model.predict_proba(vectorized_url)
        risk_score = round(float(probabilities[0][0]) * 100, 2)
        
        phishing_keywords = ['paypal-', 'secure-bank', 'login-update', 'verify-account', 'wethinkcode-portal']
        if any(keyword in input_url.lower() for keyword in phishing_keywords):
            risk_score = 95.00
        
        payment_keywords = ['pay', 'checkout', 'bank', 'shop', 'billing', 'invoice', 'boleto', 'transfer']
        is_payment_page = any(kw in input_url.lower() for kw in payment_keywords)
        
        if is_payment_page:
            if not input_url.lower().startswith("https://"):
                # CRITICAL DANGER: A payment page without HTTPS is an absolute trap
                risk_score = 100.00
                payment_safety = " DANGER: Payment page lacks HTTPS encryption! NEVER enter your card here."
            else:
                payment_safety = "Secure Gateway: Uses HTTPS encryption for online payments."
        else:
            payment_safety = "N/A (Not a detected checkout gateway)"

    if risk_score >= 30.0:
        status = "MALICIOUS"
        action_taken = "Access Blocked | Session Revoked | Admin Alerted"
    else:
        status = "SAFE"
        action_taken = "Connection Allowed"
        
    log_incident(input_url, risk_score, status, action_taken)
    
    if status == "MALICIOUS":
        return render_template("result.html", url=input_url, score=risk_score, action=action_taken)
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)

