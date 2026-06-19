import sqlite3
import os

DB_FILE = "phishguard.db"

def init_db():
    """Initializes the SQLite database and creates the threat log table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Create a table to store threat incidents
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS threat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT (datetime('now', 'localtime')),
            url TEXT NOT NULL,
            risk_score REAL NOT NULL,
            status TEXT NOT NULL,
            action_taken TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("SQLite database initialized successfully!")

def log_incident(url, risk_score, status, action_taken):
    """Inserts a new phishing or safe incident into the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS whitelist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT UNIQUE NOT NULL
        )
    ''')
    
    legit_domains = [
        'google.com', 'google.co.za', 'wethinkcode.co.za', 'github.com', 
        'takealot.com', 'hacksouth.africa', 'netflix.com', 'youtube.com', 
        'microsoft.com', 'absa.co.za', 'fnb.co.za', 'standardbank.co.za'
    ]
     
    for domain in legit_domains:
        cursor.execute("INSERT OR IGNORE INTO whitelist (domain) VALUES (?)", (domain,))
    
    def log_incident(url, risk_score, status, action_taken):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO threat_logs (url, risk_score, status, action_taken) VALUES (?, ?, ?, ?)', (url, risk_score, status, action_taken))
        conn.commit()
        conn.close()

def get_all_logs():
    """Retrieves all logged incidents to display on the dashboard."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM threat_logs ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    
    conn.close()
    return logs

if __name__ == "__main__":
    init_db()
