import network
import espnow
import time
import sys
import machine

# A WLAN interface must be active to send()/recv()
sta = network.WLAN(network.STA_IF)  # Or network.AP_IF
sta.active(True)
sta.disconnect()  # For ESP8266

e = espnow.ESPNow()
e.active(True)
peer = b'\xfc\xb4g\xf3Vx'

e.add_peer(peer)  # Must add_peer() before send()

message_count = 1

print("Starting communication...", file=sys.stdout)
led = machine.Pin(2, machine.Pin.OUT)

while True:
    # Create the message
    message = f"Message number {message_count}"
    #print(f"Sending message: {message}", file=sys.stdout)

    # Send the message
    e.send(peer, message, True)
    #print(f"Message sent: {message}", file=sys.stdout)
    led.off()
    led.value(not led.value())  # Toggle the LED state
    time.sleep(0.1)
    led.value(not led.value())
    # Wait for 2 seconds before sending the next message
    time.sleep(7.5)

    message_count += 1
    print("\n" * 25)
    print('number of messages sent = ', message_count)