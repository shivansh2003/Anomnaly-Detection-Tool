import os

def save_anomalies(anomaly_df):
    os.makedirs('data/anomalies', exist_ok=True)  # <- ensure folder exists

    anomaly_df.to_csv('data/anomalies/anomalies_detected.csv', index=False)
    anomaly_df.to_json('data/anomalies/anomalies_detected.json', orient='records', indent=2)
    anomaly_df.to_excel('data/anomalies/anomalies_detected.xlsx', index=False)
