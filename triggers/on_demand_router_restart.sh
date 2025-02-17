#!/bin/bash

CURRENT_DIR=$(pwd)
date
echo "Process Started !!"

cd /home/sv_admin/production/sermon || exit

source .venv/bin/activate
cd HardwareManagementFramework || exit

# Trigger router restart (power off, then power on)
nohup python3 main.py --on-demand-router-restart > /dev/null 2>&1 &
disown
sleep 10

cd ..
deactivate
echo "Process Ended !!"

cd "$CURRENT_DIR"
