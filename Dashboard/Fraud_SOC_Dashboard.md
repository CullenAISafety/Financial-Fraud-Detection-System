# Financial Fraud SOC Dashboard

**Date:** {{date}}

---

## Active Alerts

| Transaction ID | Account | Amount ($) | Risk Score | Status |
|----------------|--------|------------|------------|--------|
{% for alert in alerts %}
| {{ alert.transaction_id }} | {{ alert.account }} | {{ alert.amount }} | {{ alert.risk_score }} | {{ alert.status }} |
{% endfor %}

---

## Summary

- Total Transactions Processed: {{ total_txns }}
- Total Alerts: {{ total_alerts }}
- Highest Risk Transaction: {{ highest_risk_txn }}
- Average Risk Score: {{ avg_risk }}
