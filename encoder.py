from machine import Pin, UART
import time

# ===== CONFIG =====
CLK_PIN = 14
DT_PIN  = 15
GAP_MS = 500        # idle gap marks end of a bit
DEBOUNCE_MS = 1
REVERSE_DIR = False

# ===== SETUP =====
clk = Pin(CLK_PIN, Pin.IN, Pin.PULL_UP)
dt  = Pin(DT_PIN, Pin.IN, Pin.PULL_UP)

uart = UART(0, 115200)  # UART to send data

last_clk = clk.value()
last_edge_ms = time.ticks_ms()
last_debounce_ms = last_edge_ms

movement = 0
binary_data = ""
full_message = ""

# Direction calculation
def dir_sign(clk_now, dt_now):
    s = 1 if (dt_now != clk_now) else -1
    return -s if REVERSE_DIR else s

# Decode binary to character
def decode_binary(binary_str):
    try:
        return chr(int(binary_str, 2))
    except:
        return "?"

while True:
    now = time.ticks_ms()
    clk_now = clk.value()

    # Detect edge
    if clk_now != last_clk:
        if time.ticks_diff(now, last_debounce_ms) > DEBOUNCE_MS:
            movement += dir_sign(clk_now, dt.value())
            last_edge_ms = now
            last_debounce_ms = now
        last_clk = clk_now

    # End of burst → commit bit
    idle = time.ticks_diff(now, last_edge_ms)
    if movement != 0 and idle > GAP_MS:
        bit = '1' if movement > 0 else '0'
        binary_data += bit
        movement = 0

        if len(binary_data) == 8:
            char = decode_binary(binary_data)
            full_message += char
            binary_data = ""

    # Send full message if 200ms idle (much faster than 1s)
    if full_message and idle > 200:
        uart.write(full_message + "\n")  # send complete message
        print("📤 Sent full message:", full_message)
        full_message = ""

    time.sleep(0.001)

