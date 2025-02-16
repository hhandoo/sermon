#!/bin/bash

CURRENT_DIR=$(pwd)

cd /home/sv_admin/production/sermon

source .venv/bin/activate
cd HardwareManagementFramework

# Pass the command as an argument
python3 main.py --on-demand-command "$1"

cd ..
deactivate
echo "Process Ended !!"

cd "$CURRENT_DIR"
