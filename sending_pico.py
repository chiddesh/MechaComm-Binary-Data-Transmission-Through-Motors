from machine import Pin
import time
import sys
# RPI PICO GPIO PINS
IN1 = Pin(2, Pin.OUT)
IN2 = Pin(3, Pin.OUT)
IN3 = Pin(4, Pin.OUT)
IN4 = Pin(5, Pin.OUT)
pins = [IN1, IN2,IN3, IN4]
# HALF STEP SEQUENCE FOR STEPPER MOTOR
sequence = [ [1,0,0,1], [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0], [0,0,1,0], [0,0,1,1], [0,0,0,1] ]

def Move(direction,step=50,delay=0.001):
    if direction == 0:
        print("turning left - 0")
        for i in range(step):
            for pattern in sequence:
                for pin,val in zip(pins,pattern):
                    pin.value(val)
                time.sleep(delay)
    elif direction == 1:
        print("turning right - 1")
        for i in range(step):
            for pattern in reversed(sequence):
                for pin,val in zip(pins, pattern):
                    pin.value(val)
                time.sleep(delay)

def data_to_binary(data):
    result = ""
    for ch in data:
        ascii_value = ord(ch)
        binary_val = bin(ascii_value)[2:]
        
        while len(binary_val) < 8:
            binary_val = "0" + binary_val
        result += binary_val + " "
    return result.strip()



while True:
    line = sys.stdin.readline().strip()
    if line:
        print("recieved:", line)
        binary_str = data_to_binary(line)
        print("Binary Representation:", binary_str)
        
        for bit in binary_str.replace(" ", ""):
            if bit == "0":
                Move(0)
            elif bit == "1":
                Move(1)
            time.sleep(0.5)
