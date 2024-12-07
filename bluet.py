#pip install pybluez
import bluetooth

def scan_bluetooth_devices():
    print("Scanning for Bluetooth devices...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_class=False)
    if not devices:
        print("No Bluetooth devices found.")
    else:
        print(f"Found {len(devices)} device(s):")
        for addr, name in devices:
            try:
                print(f"  Device Name: {name}\n  MAC Address: {addr}\n")
            except UnicodeEncodeError:
                print(f"  Device Name: (unknown)\n  MAC Address: {addr}\n")

if __name__ == "__main__":
    scan_bluetooth_devices()
