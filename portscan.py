import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout for each connection attempt
            s.connect((host, port))
            print(f"[+] Port {port} is open.")
            return port
    except (socket.timeout, ConnectionRefusedError):
        return None

def port_scanner(host, start_port, end_port):
    print(f"Scanning {host} for open ports from {start_port} to {end_port}...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(host, p), range(start_port, end_port + 1))
    for port in results:
        if port:
            open_ports.append(port)
    print(f"\nOpen ports on {host}: {open_ports}")
    return open_ports

# Example Usage
if __name__ == "__main__":
    target_host = "scanme.nmap.org"  # Example: Replace with the target host
    start = 1
    end = 100
    port_scanner(target_host, start, end)
