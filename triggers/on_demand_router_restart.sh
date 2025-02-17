#!/bin/bash

CURRENT_DIR=$(pwd)
date
echo "Process Started !!"

cd /home/sv_admin/production/sermon || exit

source .venv/bin/activate
cd HardwareManagementFramework || exit
python3 main.py --on-demand-router-restart

cd ..
deactivate
echo "Process Ended !!"

cd "$CURRENT_DIR"
