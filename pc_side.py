import tkinter as tk
import serial
import threading
import time

# --- CONFIG --- #
PICO_SEND_PORT = "/dev/ttyACM0"     # sending Pico port
PICO_RECEIVE_PORT = "/dev/ttyACM1"  # receiving Pico port
BAUD = 115200

# --- SERIAL INIT --- #
ser_send = None
ser_receive = None

try:
    ser_send = serial.Serial(PICO_SEND_PORT, BAUD, timeout=1)
    print(f"Connected to send Pico on {PICO_SEND_PORT}")
except Exception as e:
    print(f"❌ Could not open {PICO_SEND_PORT}: {e}")

try:
    ser_receive = serial.Serial(PICO_RECEIVE_PORT, BAUD, timeout=0.01)
    print(f"Connected to receive Pico on {PICO_RECEIVE_PORT}")
except Exception as e:
    print(f"❌ Could not open {PICO_RECEIVE_PORT}: {e}")

# --- GUI APP --- #
root = tk.Tk()
root.title("Send & Receive with Pico")

tk.Label(root, text="Enter Data to Send:").pack()
entry = tk.Entry(root, width=30)
entry.pack()

text = tk.Text(root, height=20, width=60)
text.pack()

def send_to_pico():
    data = entry.get()
    if ser_send:
        ser_send.write((data + "\n").encode())
        text.insert(tk.END, f"📤 Sent: {data}\n")
        text.see(tk.END)
        entry.delete(0,tk.END)
    else:
        text.insert(tk.END, "⚠️ Send Pico not connected!\n")

tk.Button(root, text="Send", command=send_to_pico).pack(pady=5)

# --------------------- SERIAL RECEIVER --------------------- #
def process_serial_data():
    current_message = ""
    while True:
        if ser_receive and ser_receive.in_waiting:
            line = ser_receive.readline().decode(errors="ignore")
            if line:
                current_message += line
                if "\n" in current_message:
                    full_msg = current_message.strip()
                    text.insert(tk.END, f"📥 Full message received: {full_msg}\n")
                    text.see(tk.END)
                    current_message = ""
        time.sleep(0.01)

# ------------------- RUN THREADS ------------------- #
if ser_receive:
    threading.Thread(target=process_serial_data, daemon=True).start()

root.mainloop()

# Close serial on exit
if ser_send:
    ser_send.close()
if ser_receive:
    ser_receive.close()
