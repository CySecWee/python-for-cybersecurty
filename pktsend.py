from scapy.all import (
    conf, Ether, ARP, IP, ICMP, TCP, UDP, Raw, DNS, DNSQR, BOOTP, send, sendp
)

conf.verb = 0  # Suppresses Scapy's output

# Target information
target_ip = "192.168.1.100"  # Replace with target IP
#target_mac = "ff:ff:ff:ff:ff:ff"  # Replace with target MAC address
target_mac="C8:B2:9B:7F:A7:74"

# Layer 2 - Ethernet Broadcast
def send_ethernet_broadcast():
    packet = Ether(dst=target_mac) / IP(dst=target_ip)
    sendp(packet)
    print("[+] Ethernet Broadcast Sent")

# Layer 2 - ARP Request
def send_arp_request():
    packet = ARP(pdst=target_ip)
    send(packet)
    print("[+] ARP Request Sent")

# Layer 3 - ICMP (Ping)
def send_icmp_ping():
    packet = IP(dst=target_ip) / ICMP()
    send(packet)
    print("[+] ICMP Ping Sent")

# Layer 4 - TCP SYN
def send_tcp_syn():
    packet = IP(dst=target_ip) / TCP(dport=80, flags="S")
    send(packet)
    print("[+] TCP SYN Sent")

# Layer 4 - UDP Packet
def send_udp_packet():
    packet = IP(dst=target_ip) / UDP(dport=53) / Raw(load="UDP Payload")
    send(packet)
    print("[+] UDP Packet Sent")

# Application Layer - DNS Query
def send_dns_query():
    packet = IP(dst="8.8.8.8") / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com"))
    send(packet)
    print("[+] DNS Query Sent")

# Application Layer - HTTP Packet
def send_http_packet():
    packet = IP(dst=target_ip) / TCP(dport=80) / Raw(load="GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    send(packet)
    print("[+] HTTP Packet Sent")

# Application Layer - DHCP Discover
def send_dhcp_discover():
    packet = Ether(dst=target_mac) / IP(src="0.0.0.0", dst="255.255.255.255") / UDP(sport=68, dport=67) / BOOTP(chaddr="12:34:56:78:90:ab")
    sendp(packet)
    print("[+] DHCP Discover Sent")

# Application Layer - HTTPS Packet
def send_https_packet():
    packet = IP(dst=target_ip) / TCP(dport=443) / Raw(load="GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    send(packet)
    print("[+] HTTPS Packet Sent")

# Menu-Driven Packet Sender (Updated with HTTPS option)
def packet_sender_menu():
    print("\n[ Packet Sender Menu ]")
    print("1. Ethernet Broadcast")
    print("2. ARP Request")
    print("3. ICMP Ping")
    print("4. TCP SYN")
    print("5. UDP Packet")
    print("6. DNS Query")
    print("7. HTTP Packet")
    print("8. DHCP Discover")
    print("9. HTTPS Packet")  # Added HTTPS option
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")
    actions = {
        "1": send_ethernet_broadcast,
        "2": send_arp_request,
        "3": send_icmp_ping,
        "4": send_tcp_syn,
        "5": send_udp_packet,
        "6": send_dns_query,
        "7": send_http_packet,
        "8": send_dhcp_discover,
        "9": send_https_packet,  
        "10": exit,
    }

    action = actions.get(choice)
    if action:
        action()
    else:
        print("Invalid choice. Please try again.")
    packet_sender_menu()

# Entry Point
if __name__ == "__main__":
    print("** Scapy Packet Sender **")
    packet_sender_menu()
