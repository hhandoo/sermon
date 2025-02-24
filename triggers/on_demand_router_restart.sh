#!/bin/bash

DEVICE="/dev/ttyUSB0"
BAUD=115200
SESSION_NAME="nodemcu_session"

# Start a detached screen session
screen -dmS $SESSION_NAME $DEVICE $BAUD
sleep 1  # Give screen some time to start

# Send "0000" followed by Enter
screen -S $SESSION_NAME -X stuff "0000\r"

# Wait 30 seconds
sleep 30

# Send "0011" followed by Enter
screen -S $SESSION_NAME -X stuff "0011\r"

# Optional: Detach from session (keeps screen running in the background)
screen -S $SESSION_NAME -X detach
