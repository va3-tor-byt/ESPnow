
import network

def show_mac_address():
    # Initialize the WiFi interface
    wlan = network.WLAN(network.STA_IF)
    
    # Activate the interface
    wlan.active(True)
    
    # Get the MAC address
    mac = wlan.config('mac')
    
    # Format and print the MAC address
    print('MAC Address: ' + ':'.join('%02x' % b for b in mac))

# Run the function when the device boots
show_mac_address()

import Sender