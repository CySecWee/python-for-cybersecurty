#pip install python-nmap
import nmap

def nmap_port_scanner(host, ports="1-100"):
    nm = nmap.PortScanner()
    print(f"Scanning {host} for open ports ({ports}) using Nmap...")
    try:
        # Perform the scan
        nm.scan(hosts=host, ports=ports, arguments='-sS -T4')
        for host in nm.all_hosts():
            print(f"\nHost: {host} ({nm[host].hostname()})")
            print(f"State: {nm[host].state()}")
            for proto in nm[host].all_protocols():
                print(f"\nProtocol: {proto}")
                ports = nm[host][proto].keys()
                for port in sorted(ports):
                    state = nm[host][proto][port]['state']
                    print(f"Port: {port}\tState: {state}")
    except Exception as e:
        print(f"Error: {e}")

# Example Usage
if __name__ == "__main__":
    target_host = "scanme.nmap.org"  # Example target
    port_range = "1-100"  # Define port range
    nmap_port_scanner(target_host, port_range)
