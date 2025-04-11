from capture.capture import capture_packets
from converter.convert import convert_pcap_to_csv
from parser.extract import extract_features
from analyzer.analyze import analyze_traffic
from models.isolation_model import train_isolation_forest
from storage.store import save_anomalies
from visualizer.visualize import generate_visuals
from utils.logger import log_info, log_debug, log_warning, log_success
from utils.setup import setup_directories
import pandas as pd

setup_directories()


def run_tool(interface, duration):
    log_info(">> Step 1: Capturing packets")
    pcap_file = capture_packets(interface, duration)
    print(f"[DEBUG] PCAP file: {pcap_file}")

    log_info(">> Step 2: Converting to CSV")
    csv_file = convert_pcap_to_csv(pcap_file)
    print(f"[DEBUG] CSV file: {csv_file}")

    log_info(">> Step 3: Extracting features")
    features_csv = extract_features(csv_file)
    log_debug(f"Features CSV: {features_csv}")
    print(f"[DEBUG] Features CSV: {features_csv}")

    log_info(">> Step 4: Analyzing traffic")
    df = pd.read_csv(features_csv)
    analysis = analyze_traffic(df)
    print(f"[DEBUG] Analysis shape: {analysis.shape}")

    log_info(">> Step 5: Running anomaly detection")
    anomalies, model = train_isolation_forest(analysis)
    print(f"[DEBUG] Anomalies detected: {len(anomalies)}")

    if not anomalies.empty:
        log_warning(f"{len(anomalies)} anomalies detected!")
        from rich.table import Table
        table = Table(title="Anomalies Detected")

        table.add_column("Source", style="cyan")
        table.add_column("Protocol", style="magenta")
        table.add_column("Packets", justify="right", style="red")

        for _, row in anomalies.iterrows():
            table.add_row(str(row['Source']), row['Protocol'], str(row['Packet Count']))

        from rich.console import Console
        Console().print(table)
    else:
        log_success("No anomalies detected.")

    log_info("Saving results...")
    save_anomalies(anomalies)

    log_info("Generating visualizations...")
    generate_visuals(analysis)

    log_success("Network traffic analysis complete.")