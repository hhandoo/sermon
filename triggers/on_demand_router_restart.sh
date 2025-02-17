#!/bin/bash

CURRENT_DIR=$(pwd)
date
echo "Process Started !!"

cd /home/sv_admin/production/sermon || exit

source .venv/bin/activate
cd HardwareManagementFramework || exit

# Start a new tmux session for executing the script
tmux new-session -d 'python3 main.py --on-demand-router-restart'

cd ..
deactivate
echo "Process Ended !!"

cd "$CURRENT_DIR"
