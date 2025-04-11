# --------------------------- capture/capture.py ---------------------------
from scapy.all import sniff, wrpcap
import os

def capture_packets(interface, duration):
    packets = sniff(iface=interface, timeout=duration)
    output_file = f"data/raw/capture.pcap"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    wrpcap(output_file, packets)
    return output_file