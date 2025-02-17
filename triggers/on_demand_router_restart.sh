#!/bin/bash

CURRENT_DIR=$(pwd)
date
echo "Process Started !!"

cd /home/sv_admin/production/sermon || exit

source .venv/bin/activate
cd HardwareManagementFramework || exit

# Run the script that triggers the router restart in a detached background process
nohup python3 main.py --on-demand-router-restart > /dev/null 2>&1 &

# Alternatively, use SSH directly in the script if main.py is not needed
# ssh user@router "nohup sleep 5 && reboot > /dev/null 2>&1 &"

cd ..
deactivate
echo "Process Ended !!"

cd "$CURRENT_DIR"
