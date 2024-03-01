#!/bin/bash

# Update the package lists
sudo apt-get update

# Install system dependencies
sudo apt-get install -y libraspberrypi0 libraspberrypi-bin libraspberrypi-dev

# Create a virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate
