#!/bin/bash

# install_requirements.sh
# Description: Script to set up the APRS project environment on a Debian 12 VM.
# Powered by F4VSE/CT7AJM

# Updates and upgrades the system packages
echo "Updating system packages..."
sleep 2
sudo apt update && sudo apt upgrade -y
sleep 3
echo "Done!"
sleep 2

# Installs Python 3 and pip
echo "Installing Python 3 and pip..."
sleep 2
sudo apt install python3 python3-pip -y
sleep 3
echo "Done!"
sleep 2

# Installs required Python Packages
echo "Installing Required Python Packages..."
sleep 2
pip3 install aprslib requests
sleep 3
echo "Done!"
sleep 2

echo "Setup complete! You can now run the application manually by using "python3 main.py".
sleep 6
