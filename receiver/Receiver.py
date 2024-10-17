import network
import espnow
import machine
import time

# Setup WLAN and ESP-NOW
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()  # For ESP8266

e = espnow.ESPNow()
e.active(True)

# Setup LED
led = machine.Pin(2, machine.Pin.OUT)  # GPIO 2 is typical for the onboard LED
message_count = 0
# Wait to receive messages
while True:
    peer, msg = e.recv()  # Receive message and peer MAC address
    if msg:
        # Print the peer and message to the serial port
        #print(f"Received from {peer}: {msg}")
        message_count += 1
        print("\n" * 25)
        print('number of messages received = ', message_count)
        # Blink LED for 0.5 seconds to indicate message received
        time.sleep(0.5)
        led.on()
        time.sleep(0.1)
        led.off()
        time.sleep(0.1)
        led.on()
        time.sleep(0.05)
        led.off()