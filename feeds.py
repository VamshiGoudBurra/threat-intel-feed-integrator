def fetch_iocs():
    iocs = [
        {"indicator": "192.168.1.100", "type": "Malicious IP", "severity": "High"},
        {"indicator": "phishing-login.xyz", "type": "Phishing Domain", "severity": "Critical"},
        {"indicator": "abc123hash", "type": "Malware Hash", "severity": "Medium"},
        {"indicator": "fakebank-login.com", "type": "Phishing URL", "severity": "High"}
    ]
    return iocs
