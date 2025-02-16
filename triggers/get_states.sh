#!/bin/bash

CURRENT_DIR=$(pwd)

cd /home/sv_admin/production/sermon

source .venv/bin/activate
cd HardwareManagementFramework

# Run without passing any additional arguments
python3 main.py --get-states

cd ..
deactivate
echo "Process Ended !!"

cd "$CURRENT_DIR"
