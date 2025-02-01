import network
import time
import cheerlights_api
import neopixel
import machine

NUM_PIXELS = 32
DATA_PIN = 28

# Initialize NeoPixel strip
np = neopixel.NeoPixel(machine.Pin(DATA_PIN), NUM_PIXELS)

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("YOUR WIFI", "WIFI PASSWORD")
time.sleep(5)  # Allow time for connection
print(f"WiFi Connected: {wlan.isconnected()}")

# Function to update NeoPixels
def update_pixels(color):
    for i in range(NUM_PIXELS):
        np[i] = color
    np.write()

# Get the initial color
current_color = cheerlights_api.hex_to_rgb(cheerlights_api.get_current_hex())
update_pixels(current_color)
print(f"Initial color: {current_color}")

while True:
    time.sleep(5)  # Check for updates every 5 seconds
    new_color = cheerlights_api.hex_to_rgb(cheerlights_api.get_current_hex())

    if new_color != current_color:
        print(f"Color changed: {new_color}")
        update_pixels(new_color)
        current_color = new_color
    else:
        print("No change in color")
