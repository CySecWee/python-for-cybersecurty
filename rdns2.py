import dns.resolver
import dns.reversename

def reverse_dns_lookup_with_dnspython(ip_address):
    try:
        # Create a reverse pointer for the IP
        reverse_name = dns.reversename.from_address(ip_address)
        # Query the PTR record
        domain_name = dns.resolver.resolve(reverse_name, "PTR")[0]
        return str(domain_name)
    except Exception as e:
        return f"Error: {e}"

# Example Usage
ip = "8.8.8.8"
result = reverse_dns_lookup_with_dnspython(ip)
print(f"Domain name for IP {ip}: {result}")
