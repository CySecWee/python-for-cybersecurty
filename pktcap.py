from scapy.all import sniff, get_if_list, IP, TCP, UDP, DNS, Raw
import logging

# Configure logging to log captured packets
logging.basicConfig(filename="packet_capture.log", level=logging.INFO)

# Function to handle captured packets
def packet_handler(packet):
    try:
        # Log the raw packet data
        logging.info(f"Packet captured: {packet.summary()}")

        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            protocol = packet[IP].proto
            packet_length = len(packet)

            print(f"IP Packet - Source: {ip_src} -> Destination: {ip_dst}, Protocol: {protocol}, Length: {packet_length} bytes")

            # If it's a TCP packet, analyze further
            if TCP in packet:
                tcp_src_port = packet[TCP].sport
                tcp_dst_port = packet[TCP].dport
                print(f"TCP Packet - Source Port: {tcp_src_port} -> Destination Port: {tcp_dst_port}")

            # If it's a UDP packet, analyze further
            elif UDP in packet:
                udp_src_port = packet[UDP].sport
                udp_dst_port = packet[UDP].dport
                print(f"UDP Packet - Source Port: {udp_src_port} -> Destination Port: {udp_dst_port}")

            # If it's a DNS packet, extract query details
            elif DNS in packet:
                dns_query = packet[DNS].qd.qname.decode("utf-8")
                print(f"DNS Query - {dns_query}")

            # Handle Raw payloads (non-application data)
            if Raw in packet:
                raw_data = packet[Raw].load
                print(f"Raw Data: {raw_data[:30]}...")  # print first 30 bytes of the raw payload
        else:
            print("Non-IP packet captured")

    except Exception as e:
        print(f"Error processing packet: {e}")

# Function to start sniffing and analyzing packets
def start_sniffing(interface, packet_count=10):
    """
    Start sniffing the network interface for a specified number of packets.
    """
    print(f"Starting packet capture on interface {interface}...")
    sniff(iface=interface, prn=packet_handler, count=packet_count, store=False)

if __name__ == "__main__":
    # Dynamically get the list of available network interfaces
    available_interfaces = get_if_list()
    
    print("Available network interfaces:")
    for i, iface in enumerate(available_interfaces, 1):
        print(f"{i}. {iface}")
    
    # Prompt the user to choose an interface
    interface_choice = int(input(f"Enter network interface number (1-{len(available_interfaces)}): ")) - 1
    interface = available_interfaces[interface_choice]
    
    # Start sniffing on the selected interface
    start_sniffing(interface=interface, packet_count=20)
