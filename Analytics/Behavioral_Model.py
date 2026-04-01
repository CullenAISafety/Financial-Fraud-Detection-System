import pandas as pd
from sklearn.ensemble import IsolationForest

def train_model(transactions):
    """
    Train a simple anomaly detection model using transaction amounts
    """
    df = pd.DataFrame(transactions)
    X = df[["amount"]].values
    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)
    return model

def predict_anomalies(model, transactions):
    df = pd.DataFrame(transactions)
    X = df[["amount"]].values
    preds = model.predict(X)
    df["anomaly"] = preds
    return df[df["anomaly"] == -1].to_dict(orient="records")
