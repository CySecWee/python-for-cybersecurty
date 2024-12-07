import socket

def reverse_dns_lookup(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror as e:
        return f"Error: {e}"

# Example Usage
ip = "8.8.8.8"  # Example: Google's public DNS server
result = reverse_dns_lookup(ip)
print(f"Domain name for IP {ip}: {result}")
