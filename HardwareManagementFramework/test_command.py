import serial
import time

# Replace with your actual serial port (e.g., "/dev/ttyUSB0" on Linux)
SERIAL_PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

try:
    # Open serial connection
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Allow time for NodeMCU to initialize

    # Send a command
    command = "1111\n"  # Example command to turn on an LED
    ser.write(command.encode())  # Send as bytes
    print(f"Sent: {command.strip()}")

    # Read response (optional)
    response = ser.readline().decode().strip()
    print(f"Received: {response}")

    # Close serial connection
    ser.close()

except Exception as e:
    print(f"Error: {e}")
