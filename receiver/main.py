'''from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "https://raw.githubusercontent.com/<username>/<repo_name>/<branch_name>"
'''
import network

def show_mac_address():
    # Initialize the WiFi interface
    wlan = network.WLAN(network.STA_IF)
    
    # Activate the interface
    wlan.active(True)
    
    # Get the MAC address
    mac = wlan.config('mac')
    
    # Format and print the MAC address
    print(mac)

# Run the function when the device boots
show_mac_address()

import Receiver