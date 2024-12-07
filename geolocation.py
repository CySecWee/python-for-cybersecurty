#pip install ipinfo

import ipinfo

# Replace with your IPinfo API token
ACCESS_TOKEN = "142.251.12.101"

def geolocate_ip(ip_address):
    try:
        handler = ipinfo.getHandler(ACCESS_TOKEN)
        details = handler.getDetails(ip_address)
        return {
            "IP Address": ip_address,
            "City": details.city,
            "Region": details.region,
            "Country": details.country,
            "Location": details.loc,  # Latitude and Longitude
            "Organization": details.org,
            "Postal": details.postal
        }
    except Exception as e:
        return {"error": str(e)}

# Example Usage
if __name__ == "__main__":
    ip = "8.8.8.8"  # Example: Google's public DNS server
    geolocation_info = geolocate_ip(ip)
    print("Geolocation Information:")
    for key, value in geolocation_info.items():
        print(f"{key}: {value}")

