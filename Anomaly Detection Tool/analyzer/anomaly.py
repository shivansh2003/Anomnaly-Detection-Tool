import pandas as pd

def detect_anomalies(df):
    anomalies = []

    # Detect IPs with packet count > threshold
    threshold = df['Packet Count'].mean() + 2 * df['Packet Count'].std()
    high_traffic = df[df['Packet Count'] > threshold]

    for _, row in high_traffic.iterrows():
        anomalies.append({
            'Source': row['Source'],
            'Protocol': row['Protocol'],
            'Packets': row['Packet Count'],
            'Type': 'High Traffic'
        })

    return pd.DataFrame(anomalies)
