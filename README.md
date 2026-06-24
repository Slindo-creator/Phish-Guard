PhishGuard AI — Real-Time Threat Mitigation Engine

Core Engineering Features
* **Defense-in-Depth Pipeline**: Implements an elite 3-layer verification matrix (Database Whitelist Static Heuristic Rules Machine Learning Engine).
* **Automated Threat Interception**: Instantly drops execution threads when encountering critical risks ((Risk >= 60%), redirecting users to a standalone `result.html` mitigation screen.
* **Incident Log Engine**: Writes all transactional events dynamically to a local SQLite database complete with localized South African Standard Time (SAST) stamps.
* **Session Revocation Simulator**: Simulates high-priority SOC responses including credential freezes, session terminations, and security analyst alerts.


Project Directory Schema

Phish-Guard/
│
├── data/
│   └── phishing_urls.csv     # Training target data inputs
├── templates/
│   ├── base.html             # Master theme document layout
│   ├── dashboard.html        # Main traffic monitoring center
│   └── result.html           # Intercept and isolation template
│
├── model.py                  # Scikit-Learn model execution script
├── database.py               # SQLite infrastructure instantiation script
└── app.py                    # Core web routing configuration engine
```

Install Required Application Dependencies
This command sequence inside to active terminal console to download core system binaries:
```bash
pip install flask scikit-learn pandas numpy
```

Initialize the AI Prediction Assets
Train and save the pipeline models onto your physical hard drive by running:
```bash
python model.py
```
*This will produce `phishing_model.pkl` and `vectorizer.pkl` dependencies directly into your workspace root.*


Seed the Transaction Tables & Fire Up the Server
Initialize your SQLite log files and boot the engine:
```bash
python database.py
python app.py
```
Navigate to your local browser interface address: `http://127.0.0.1:5000`


Live Code Demonstration Showcase
Click the link below to watch the complete 5–10 minute implementation walkthrough, repository commit architecture review, and live exploitation interception validation

[WATCH MY PHISHGUARD AI VIDEO DEMONSTRATION ON YOUTUBE](will fill after fliming video)