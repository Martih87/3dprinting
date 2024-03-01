#!/bin/bash

# Update the package lists
sudo apt-get update

# Install system dependencies
sudo apt-get install -y libraspberrypi0 libraspberrypi-bin libraspberrypi-dev

# Install Python dependencies
pip install -r requirements.txt
