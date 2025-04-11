# --------------------------- storage/save.py ---------------------------
import os

def save_results(dataframe):
    os.makedirs("data/processed", exist_ok=True)
    dataframe.to_csv("data/processed/analysis.csv", index=False)