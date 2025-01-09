#!/bin/bash


CURRENT_DIR=$(pwd)
echo "Process Started !!"
cd /home/kaeshur/Documents/sermon



source .venv/bin/activate
cd HardwareManagementFramework
python3 main.py
cd ..
deactivate
echo "Process Ended !!"
cd "$CURRENT_DIR"

