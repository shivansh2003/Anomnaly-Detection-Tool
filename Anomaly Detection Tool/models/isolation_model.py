import pandas as pd
from sklearn.ensemble import IsolationForest

def train_isolation_forest(df):
    model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)

    # Select numerical features
    X = df[['Packet Count']].copy()
    model.fit(X)
    
    df['Anomaly'] = model.predict(X)  # -1 = anomaly, 1 = normal
    return df[df['Anomaly'] == -1], model
