# Financial Fraud Case Reports

**Date:** {{date}}

---

{% for alert in alerts %}
## Case Report: Transaction {{ alert.transaction_id }}

- **Account:** {{ alert.account }}
- **Transaction Amount:** ${{ alert.amount }}
- **Risk Score:** {{ alert.risk_score }}
- **Status:** {{ alert.status }}

### Analysis:
- Detected by: Financial Fraud Detection System v1.0
- Risk factors:
  {% if alert.risk_score >= 70 %}
  - High severity alert (Immediate review required)
  {% elif alert.risk_score >= 50 %}
  - Medium severity (Investigate pattern)
  {% else %}
  - Low severity (Monitor)
  {% endif %}

### Recommended Action:
- Freeze account or transaction for high-risk cases
- Notify fraud analyst
- Log case in investigation system
---
{% endfor %}
