#pip install python-whois dnspython

import whois
import dns.resolver

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return {
            "domain_name": w.domain_name,
            "registrar": w.registrar,
            "creation_date": w.creation_date,
            "expiration_date": w.expiration_date,
            "name_servers": w.name_servers,
            "status": w.status,
            "emails": w.emails,
        }
    except Exception as e:
        return {"error": str(e)}

def get_dns_records(domain):
    records = {}
    try:
        # A Record
        a_records = [str(ip) for ip in dns.resolver.resolve(domain, "A")]
        records["A"] = a_records
    except Exception:
        records["A"] = None

    try:
        # MX Record
        mx_records = [str(r.exchange) for r in dns.resolver.resolve(domain, "MX")]
        records["MX"] = mx_records
    except Exception:
        records["MX"] = None

    try:
        # NS Record
        ns_records = [str(ns) for ns in dns.resolver.resolve(domain, "NS")]
        records["NS"] = ns_records
    except Exception:
        records["NS"] = None

    try:
        # TXT Record
        txt_records = [str(txt) for txt in dns.resolver.resolve(domain, "TXT")]
        records["TXT"] = txt_records
    except Exception:
        records["TXT"] = None

    return records

# Example Usage
domain = "google.com"
whois_info = get_whois_info(domain)
dns_info = get_dns_records(domain)

print("WHOIS Information:")
print(whois_info)

print("\nDNS Records:")
print(dns_info)
