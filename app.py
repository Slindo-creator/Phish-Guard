from flask import Flask, render_template, request, redirect, url_for
import pickle
import os
import numpy as np
from database import log_incident, get_all_logs, init_db,is_whitelisted

def url_tokenizer(url):
    return url.split('/')
app = Flask(__name__)

# Ensure database tables exist when the server starts
if not os.path.exists("phishguard.db"):
    init_db()

# Load the saved AI assets
try:
    with open('phishing_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('vectorizer.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)
    print("AI Model and Vectorizer loaded successfully!")
except Exception as e:
    print(f"Error loading AI files: {e}. Please run model.py first.")

# This helper is needed so the unpickled vectorizer knows how to split text
def url_tokenizer(url):
    return url.split('/')

@app.route('/')
def dashboard():
    # Fetches all historical scans from the database to display a live feed
    logs = get_all_logs()
    return render_template('dashboard.html', logs=logs)

@app.route('/scan', methods=['POST'])
def scan_url():
    input_url = request.form.get('url', '').strip()
    
    if not input_url:
        return redirect(url_for('dashboard'))
    
    if is_whitelisted(input_url):
        risk_score = 0.00
    else:     
        vectorized_url = vectorizer.transform([input_url]) 
        probabilities = model.predict_proba(vectorized_url)[0]
        risk_score = round(float(probabilities[1]) * 100, 2)
    
    if risk_score >= 60.0:
        status = "MALICIOUS"
        action_taken = "Access Blocked | Session Revoked | Admin Alerted"
        response_template = "result.html"
    else:
        status = "SAFE"
        action_taken = "Connection Allowed"
        response_template = "dashboard.html"
        
    # 3. Save the event to your database log file
    log_incident(input_url, risk_score, status, action_taken)
    
    # If malicious, redirect to the block screen; otherwise, refresh the dashboard
    if status == "MALICIOUS":
        return render_template(response_template, url=input_url, score=risk_score, action=action_taken)
    
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
