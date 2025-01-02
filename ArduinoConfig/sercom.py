import serial
import time

# Open the serial port
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)  # Replace with your serial port
time.sleep(2)  # Give Arduino time to reset

# Write a simple command
ser.write(b"1 0 1 0 1 0 1 1\n")

# Read the response from Arduino
while True:
    line = ser.readline().decode("utf-8").strip()  # Read line and decode it
    if line:
        print("Received:", line)  # Print the response
        break  # Stop after the first response
    time.sleep(0.1)  # Wait a bit before trying again

ser.close()
