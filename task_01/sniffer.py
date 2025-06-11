# sniffer.py

import argparse
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP

LOG_FILE = "packet_log.txt"

def log_packet(info):
    with open(LOG_FILE, "a") as log:
        log.write(info + "\n")

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        protocol_name = {1: "ICMP", 6: "TCP", 17: "UDP"}.get(proto, str(proto))

        log_info = f"[{timestamp}] {protocol_name} Packet: {src_ip} -> {dst_ip}"

        if TCP in packet:
            payload = bytes(packet[TCP].payload).decode(errors='ignore')
            log_info += f"\n    TCP Payload: {payload}"
        elif UDP in packet:
            payload = bytes(packet[UDP].payload).decode(errors='ignore')
            log_info += f"\n    UDP Payload: {payload}"
        elif ICMP in packet:
            log_info += "\n    ICMP Packet"

        print(log_info)
        log_packet(log_info)

def main():
    parser = argparse.ArgumentParser(description="Python Network Sniffer using Scapy")
    parser.add_argument("-i", "--interface", help="Network interface (e.g., eth0, wlan0)", default=None)
    parser.add_argument("-f", "--filter", help="BPF filter (e.g., 'tcp', 'udp', 'port 80')", default="")
    args = parser.parse_args()

    print("[*] Starting packet sniffer... Press Ctrl+C to stop.")
    sniff(iface=args.interface, filter=args.filter, prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
