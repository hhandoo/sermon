import serial
import time


ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
time.sleep(2)


ser.write(b"0 0 0 0 1 0 1 1\n")


while True:
    line = ser.readline().decode("utf-8").strip()
    if line:
        print("Received:", line)
        break
    time.sleep(0.1)

ser.close()
