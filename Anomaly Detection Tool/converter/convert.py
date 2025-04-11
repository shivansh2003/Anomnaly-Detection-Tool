def convert_pcap_to_csv(pcap_file):
    import pyshark
    import csv
    import os

    cap = pyshark.FileCapture(pcap_file)
    output_file = os.path.join('data', 'processed', 'captured_traffic.csv')
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['No.', 'Time', 'Source', 'Destination', 'Protocol', 'Length'])

        for i, packet in enumerate(cap):
            try:
                src = packet.ip.src if hasattr(packet, 'ip') else 'N/A'
                dst = packet.ip.dst if hasattr(packet, 'ip') else 'N/A'
                proto = packet.transport_layer if hasattr(packet, 'transport_layer') else 'N/A'
                length = packet.length
                writer.writerow([i + 1, packet.sniff_time, src, dst, proto, length])
            except AttributeError:
                # Skips packets that don’t have expected attributes
                continue

    cap.close()
    return output_file
