# --------------------------- analyzer/analyze.py ---------------------------
import pandas as pd

def analyze_traffic(df):
    print("[DEBUG] Columns in DataFrame:", df.columns.tolist())
    grouped = df.groupby(['Source', 'Protocol']).agg({'Packet Count': ['count', 'mean']})
    grouped.columns = ['Packet Count', 'Avg Length']
    grouped = grouped.reset_index()
    return grouped