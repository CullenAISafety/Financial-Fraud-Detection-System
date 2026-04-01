def generate_alert(transaction, score):
    return {
        "transaction_id": transaction["transaction_id"],
        "account": transaction["account"],
        "risk_score": score,
        "status": "SUSPICIOUS" if score > 50 else "OK"
    }
