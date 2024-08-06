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

# Define variables
PROJECT_DIR="$HOME/fogos-2-aprs-main"
SERVICE_NAME="fogos-2-aprs.service"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME"

# Create systemd service file
echo "Creating systemd service file..."
sleep 3
sudo bash -c "cat > $SERVICE_FILE" << EOL
[Unit]
Description=fogos-2-aprs
After=network.target

[Service]
WorkingDirectory=$PROJECT_DIR
ExecStart=/usr/bin/python3 main.py
User=$USER
Group=$USER
Restart=always
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
EOL
sleep 2

# Set correct permissions for the service file
echo "Setting permissions for systemd service file..."
sudo chmod 644 $SERVICE_FILE
sleep 2

# Reload systemd to recognize the new service
echo "Reloading systemd daemon..."
sudo systemctl daemon-reload
sleep 2

# Enable the service to start on boot
echo "Enabling service to start on boot..."
sudo systemctl enable $SERVICE_NAME
sleep 3

# Start the service immediately
echo "Starting the service..."
sudo systemctl start $SERVICE_NAME
sleep 3

# Output status of the service
echo "Checking service status..."
sudo systemctl status $SERVICE_NAME
sleep 3

echo "Done! The setup is fully complete! fogos-2-aprs is now installed and running."
sleep 6

