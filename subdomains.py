#pip install requests
import requests

def check_subdomain(domain, subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        # Send a GET request to the subdomain
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True, url
    except requests.ConnectionError:
        pass
    return False, None

def scan_subdomains(domain, subdomains_list):
    found_subdomains = []
    for subdomain in subdomains_list:
        is_valid, url = check_subdomain(domain, subdomain)
        if is_valid:
            print(f"[+] Found: {url}")
            found_subdomains.append(url)
        else:
            print(f"[-] Not Found: {subdomain}.{domain}")
    return found_subdomains

# Example Usage
if __name__ == "__main__":
    # The domain to scan
    target_domain = "example.com"
    
    # A list of subdomains to test (can be extended)
    test_subdomains = [
        "www",
        "mail",
        "ftp",
        "test",
        "dev",
        "staging",
        "blog",
        "api"
    ]
    
    print(f"Scanning for subdomains of {target_domain}...\n")
    found = scan_subdomains(target_domain, test_subdomains)
    
    print("\nFound Subdomains:")
    for subdomain in found:
        print(subdomain)
