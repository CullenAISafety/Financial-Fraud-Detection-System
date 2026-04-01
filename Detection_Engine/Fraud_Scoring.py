def score_transaction(transaction, patterns):
    """
    Simple risk scoring function:
    - High amount = higher score
    - Suspicious location = +20 points
    """
    score = 0
    amount = transaction.get("amount", 0)
    location = transaction.get("location", "")

    # High transaction amount
    if amount >= patterns.get("high_amount_threshold", 10000):
        score += 40
    elif amount >= 5000:
        score += 20

    # Suspicious location
    if location in patterns.get("suspicious_locations", []):
        score += 20

    # Could add more rules: repeat transactions, time anomalies, etc.
    return score
