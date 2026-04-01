import json
from datetime import datetime
from detection_engine.transaction_monitor import load_transactions, monitor_transactions

# File paths
TRANSACTION_FILE = "data/transaction_samples.json"
PATTERN_FILE = "data/fraud_patterns.json"
ALERT_FILE = "alerts/fraud_alerts.json"
SOC_DASHBOARD_FILE = "dashboard/fraud_soc_dashboard.md"
CASE_REPORT_FILE = "investigations/fraud_case_reports.md"

# 1. Load transactions and fraud patterns
transactions = load_transactions(TRANSACTION_FILE)
with open(PATTERN_FILE) as f:
    fraud_patterns = json.load(f)

# 2. Detect anomalies and generate alerts
alerts = monitor_transactions(transactions, fraud_patterns)

# Save alerts to JSON
with open(ALERT_FILE, "w") as f:
    json.dump(alerts, f, indent=4)

print(f"{len(alerts)} alerts generated.")

# 3. Generate SOC dashboard (Markdown)
total_txns = len(transactions)
total_alerts = len(alerts)
highest_risk_txn = max(alerts, key=lambda x: x["risk_score"], default={"transaction_id": "N/A"})["transaction_id"]
avg_risk = round(sum([a["risk_score"] for a in alerts])/total_alerts, 2) if total_alerts else 0

dashboard_content = f"""# Financial Fraud SOC Dashboard

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Active Alerts

| Transaction ID | Account | Amount ($) | Risk Score | Status |
|----------------|--------|------------|------------|--------|
"""

for alert in alerts:
    dashboard_content += f"| {alert['transaction_id']} | {alert['account']} | {alert['amount']} | {alert['risk_score']} | {alert['status']} |\n"

dashboard_content += f"""
---

## Summary

- Total Transactions Processed: {total_txns}
- Total Alerts: {total_alerts}
- Highest Risk Transaction: {highest_risk_txn}
- Average Risk Score: {avg_risk}
"""

with open(SOC_DASHBOARD_FILE, "w") as f:
    f.write(dashboard_content)

print(f"SOC dashboard updated: {SOC_DASHBOARD_FILE}")

# 4. Generate Case Reports (Markdown)
case_report_content = f"# Financial Fraud Case Reports\n\n**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n---\n\n"

for alert in alerts:
    case_report_content += f"""## Case Report: Transaction {alert['transaction_id']}

- **Account:** {alert['account']}
- **Transaction Amount:** ${alert['amount']}
- **Risk Score:** {alert['risk_score']}
- **Status:** {alert['status']}

### Analysis:
- Detected by: Financial Fraud Detection System v1.0
- Risk factors:
"""
    if alert["risk_score"] >= 70:
        case_report_content += "- High severity alert (Immediate review required)\n"
    elif alert["risk_score"] >= 50:
        case_report_content += "- Medium severity (Investigate pattern)\n"
    else:
        case_report_content += "- Low severity (Monitor)\n"

    case_report_content += """
### Recommended Action:
- Freeze account or transaction for high-risk cases
- Notify fraud analyst
- Log case in investigation system
---
"""

with open(CASE_REPORT_FILE, "w") as f:
    f.write(case_report_content)

print(f"Case reports generated: {CASE_REPORT_FILE}")
