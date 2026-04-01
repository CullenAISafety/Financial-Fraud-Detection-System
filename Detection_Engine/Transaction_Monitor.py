import json
from detection_engine.anomaly_detection import detect_anomaly

def load_transactions(file_path):
    with open(file_path) as f:
        return json.load(f)

def monitor_transactions(transactions, patterns):
    alerts = []
    for txn in transactions:
        alert = detect_anomaly(txn, patterns)
        if alert:
            alerts.append(alert)
    return alerts
