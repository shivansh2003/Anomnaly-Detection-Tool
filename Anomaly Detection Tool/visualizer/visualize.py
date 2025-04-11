import matplotlib.pyplot as plt
import numpy as np
import os

def generate_visuals(df):
    # Bar chart as before
    grouped = df.groupby('Protocol')['Packet Count'].sum()
    colors = ['red' if proto in df[df['Anomaly'] == -1]['Protocol'].values else 'skyblue'
              for proto in grouped.index]

    plt.figure(figsize=(10, 6))
    grouped.plot(kind='bar', color=colors)
    plt.title('Packet Count by Protocol (ML Anomalies in Red)')
    plt.xlabel('Protocol')
    plt.ylabel('Packet Count')
    plt.tight_layout()
    os.makedirs('data/processed', exist_ok=True)
    plt.savefig('data/processed/protocol_distribution_with_anomalies.png')
    plt.show()

    # Time-based anomaly chart (simulated time index)
    if 'Anomaly' in df.columns:
        df = df.reset_index(drop=True)
        df['Time'] = np.arange(len(df))  # Fake time just for plotting

        plt.figure(figsize=(10, 5))
        plt.plot(df['Time'], df['Packet Count'], label='Traffic')
        plt.scatter(df[df['Anomaly'] == -1]['Time'], df[df['Anomaly'] == -1]['Packet Count'],
                    color='red', label='Anomalies', zorder=5)
        plt.title("Packet Count Over Time with Anomalies")
        plt.xlabel("Time (sample index)")
        plt.ylabel("Packet Count")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.savefig('data/processed/traffic_over_time_with_anomalies.png')
        plt.show()
