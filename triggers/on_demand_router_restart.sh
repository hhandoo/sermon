#!/bin/bash

CURRENT_DIR=$(pwd)
date
echo "Process Started !!"
cd /home/sv_admin/production/sermon || exit

source .venv/bin/activate
cd HardwareManagementFramework || exit
nohup python3 main.py --on-demand-router-restart > output.log 2>&1 &
cd ..
deactivate
echo "Process Ended !!"
cd "$CURRENT_DIR"
