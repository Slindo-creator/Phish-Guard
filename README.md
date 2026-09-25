PhishGuard AI — Real-Time Threat Mitigation Engine

To run this project on a modern Linux or Mac system, please follow these steps to avoid environment blocks:

### 1. Set up a Virtual Environment
Open your terminal inside the project folder and run:
```bash
python3 -m venv venv
```

### 2. Activate the Environment
Turn on the safe sandbox environment:
```bash
source venv/bin/activate
```

### 3. Install All Dependencies
Install the required libraries from the checklist:
```bash
pip install -r requirements.txt
```

### 4. Build the Machine Learning Matrix
Train your Scikit-Learn classification pipelines on your local dataset and export the prediction assets (`.pkl`) directly onto your workspace root:
```bash
python model.py
```*This will produce `phishing_model.pkl` and `vectorizer.pkl` dependencies directly into your workspace root.* 

### 5. Instantiate Transaction Tables & Launch
Seed your operational SQLite schemas and boot the live Flask inspection engine:
```bash
python database.py
python app.py
```
Once initialized, navigate to the administrative visual panel in your web browser: **`http://127.0.0.1:5000`**

---

## Core Engineering Features


* **Elite Defense-in-Depth Pipeline:** Implements a strict 3-tier validation matrix (SQLite Whitelist Overrides ➔ Tokenized Keyword Heuristics ➔ Scikit-Learn Machine Learning Evaluation).
* **Universal Malicious Link Neutralization:** The core AI engine screens for all profiles of online danger, including **fake portal clones, malware vectors, and credential harvesting paths**, stripping away structural evasion attempts.
* **Online Payment Safety Scanner:** Actively targets financial transaction gateway keywords (e.g., `checkout`, `pay`, `boleto`). If an unencrypted payment path lacks active `https://` encryption, it triggers an instant structural override to **100% Risk**.
* **Proactive Proximity Blocking:** Operates under a rigorous **30% AI Risk Threshold** limit to catch emerging and borderline phishing links instantly rather than traditional relaxed standard models.
* **Incident Log Registry Engine:** Transacts all operational logs and interception events dynamically to your local database complete with localized South African Standard Time (**SAST**) tracking logs.
* **Visual Tech-Grey Interface Layout:** Styled explicitly with a premium t

---

## Project Directory Schema

```text
Phish-Guard/
│
├── data/
│   └── phishing_site_urls.csv   # Mixed URL training target data inputs
│
├── templates/
│   ├── base.html                # Master theme document frame configuration
│   ├── dashboard.html           # Tech-grey curved inline monitoring panel
│   └── result.html              # Intercept, isolation, and warning layout
│
├── app.py                       # Core web routing & custom mitigation rules
├── database.py                  # SQLite infrastructure configuration utility
├── model.py                     # Scikit-Learn mapping & training processing script
├── requirements.txt             # Project system architecture requirements index
│
├── phishguard.db                # Standalone transactional SQLite database
├── phishing_model.pkl           # Trained Logistic Regression classification model
└── vectorizer.pkl               # TfidfVectorizer numerical data pipeline asset
```

---

## Demonstration Showcases

When showcasing the system architecture live or evaluating pipeline performance, test these exact baseline vectors to demonstrate the rules engine:

1. **`https://google.com`**  
   *Expected Result:* Allowed through smoothly with a **0.0% Risk Score** pattern.
2. **`netflix-login-verify-account.com`**  
   *Expected Result:* Flags text pattern matches, scores high on the AI engine, and is immediately blocked.
3. **`http://my-fake-shop.net`**  
   *Expected Result:* Triggered by the payment scanner, flagged for missing active `https://` encryption, and immediately clamped with a **100% Malicious Block** warning box.

---
Your verification code:
WTC-ZL5564XR


##Live Video Demonstration Walkthrough

Click the link below to watch the complete 5–10 minute implementation walkthrough, repository commit architecture review, and live exploitation interception validation:

 **[WATCH MY PHISHGUARD AI VIDEO DEMONSTRATION ON YOUTUBE](https://youtu.be/NV3J5IpDHWA)**
