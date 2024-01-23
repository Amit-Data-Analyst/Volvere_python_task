import psutil

def get_mac_addresses():
    try:
        # Get a list of network interfaces
        interfaces = psutil.net_if_addrs()

        # Initialize variables to store MAC addresses
        wifi_mac = None
        ethernet_mac = None

        # Iterate through network interfaces
        for interface, addresses in interfaces.items():
            for address in addresses:
                if address.family == psutil.AF_LINK:
                    mac_address = address.address

                    # Identify WiFi and Ethernet interfaces based on their names
                    if "Wireless" in interface or "Wi-Fi" in interface:
                        wifi_mac = mac_address
                    elif "Ethernet" in interface:
                        ethernet_mac = mac_address

        return wifi_mac, ethernet_mac

    except Exception as e:
        return None, None

if __name__ == "__main__":
    wifi_mac, ethernet_mac = get_mac_addresses()

    if wifi_mac is not None:
        print(f"WiFi MAC Address: {wifi_mac}")
    else:
        print("WiFi MAC Address not found.")

    if ethernet_mac is not None:
        print(f"Ethernet MAC Address: {ethernet_mac}")
    else:
        print("Ethernet MAC Address not found.")
