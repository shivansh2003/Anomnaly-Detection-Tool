import os

def setup_directories():
    folders = [
        'data/raw', 'data/processed', 'data/anomalies',
        'models', 'logs'
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
