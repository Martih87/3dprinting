#!/bin/bash

# Update the package lists
sudo apt-get update

# Install system dependencies
sudo apt-get install -y libraspberrypi0 libraspberrypi-bin libraspberrypi-dev
# pip for python packages
sudo apt-get install -y pip git vim


# Install Python dependencies
pip install -r requirements.txt
