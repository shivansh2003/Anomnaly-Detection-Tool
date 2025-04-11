import pandas as pd
import os

def extract_features(csv_file):
    df = pd.read_csv(csv_file)

    # Simple aggregation: count packets per source IP and protocol
    grouped = df.groupby(['Source', 'Protocol']).size().reset_index(name='Packet Count')

    output_file = os.path.join('data', 'processed', 'features.csv')
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    grouped.to_csv(output_file, index=False)

    return output_file
