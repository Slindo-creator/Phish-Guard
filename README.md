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

