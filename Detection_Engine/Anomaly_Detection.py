from detection_engine.fraud_scoring import score_transaction

def detect_anomaly(transaction, patterns):
    """
    Checks a transaction against known fraud patterns
    """
    score = score_transaction(transaction, patterns)
    if score > 50:  # threshold for alert
        return {
            "transaction_id": transaction["transaction_id"],
            "account": transaction["account"],
            "amount": transaction["amount"],
            "risk_score": score
        }
    return None
