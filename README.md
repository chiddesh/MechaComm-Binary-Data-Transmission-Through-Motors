# MotorComm: Unconventional Data Transfer Through Motor

MotorComm is an innovative project that demonstrates **mechanical data transmission** using motors and rotary encoders. It provides a creative way to send and receive data without traditional networking, relying purely on motor rotations to encode and decode information.

---

## How It Works

User Input (Text)
│
▼
GUI Application
│
▼
Convert Text → Binary
│
▼
Motor Rotation
(Left=0, Right=1)
│
▼
Receiving Pico + Rotary Encoder
│
▼
Decode Binary → Text
│
▼
Display Received Message

yaml
Copy code

**Sending Side (GUI + Pico):**

- User enters text in the GUI.
- Text is converted to **binary**.
- Motor rotates:
  - **Left rotation = 0**
  - **Right rotation = 1**
- Each character is transmitted as a series of motor rotations.

**Receiving Side (Pico + Rotary Encoder):**

- Reads motor rotations using a **rotary encoder**.
- Decodes binary sequences back into **original characters**.
- Displays the reconstructed text in the GUI.

---

## Features

- Mechanical Data Transmission: No Wi-Fi, Bluetooth, or wired communication needed.
- Binary Encoding/Decoding: Real-time conversion of text to binary and back.
- Interactive GUI: Easy-to-use interface for sending and receiving messages.
- Educational & Demonstrative: Learn about digital communication, encoding, and robotics.

---

## Applications

- Secure communication in restricted environments.
- Teaching **binary encoding and decoding**.
- Robotics backup communication systems.
- Interactive or artistic installations demonstrating physical data transfer.
- Novelty educational gadgets and DIY electronics projects.

---

## Project Structure

MotorComm/
│
├─ gui.py # Tkinter GUI for sending and receiving messages
├─ pico_encoder.py # Pico code to decode motor rotations into text
├─ README.md # Project documentation
└─ ... # Additional scripts or resources

yaml
Copy code

---

## How to Run

1. **Flash the Raspberry Pi Pico** (both sending and receiving) with MicroPython:

   - Download the latest MicroPython UF2 file for Pico from [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
   - Hold **BOOTSEL**, plug the Pico into your PC, and drag the UF2 file onto the Pico.

2. **Download this project** from GitHub:

```bash
git clone https://github.com/yourusername/MotorComm.git
```

Upload the scripts to each Pico using Thonny:

Sending Pico: sending_pico.py

Receiving Pico: encoder.py

Connect the hardware:

Sending Pico with stepper motor.

Receiving Pico with rotary encoder.

Run the GUI on your PC (optional for monitoring):

bash
Copy code
python pc_side.py
Enter text in the GUI and click Send.

Sending Pico converts text to binary → rotates the motor.

Receiving Pico decodes motor rotations → reconstructs text.

View the decoded message on the PC GUI or Pico console.

Requirements
Raspberry Pi Pico (2 boards: sending and receiving)

Stepper motor (sending Pico)

Rotary encoder (receiving Pico)

MicroPython firmware on both Picos

Python 3.x on your PC

Tkinter (pip install tk if not included)

PySerial (pip install pyserial) for GUI-PC communication

Features
Mechanical Data Transmission: No Wi-Fi, Bluetooth, or wired communication needed.

Binary Encoding/Decoding: Real-time conversion of text to binary and back.

Interactive GUI: Send and view messages easily.

Educational & Demonstrative: Learn about digital communication, encoding, and robotics.

Applications
Secure communication in restricted environments.

Teaching binary encoding and decoding.

Robotics backup communication systems.

Interactive or artistic installations demonstrating physical data transfer.

Novelty educational gadgets and DIY electronics projects.

Future Improvements
Add message integrity checks (checksum).

Increase speed of transmission with optimized rotation encoding.

Expand to multiple motor channels for parallel data transfer.

Integrate with IoT applications for hybrid mechanical-electronic communication.

License
MIT License – Free to use, modify, and distribute.

Author
Chiddesh – CSE Cyber Security, Easwari Engineering College
