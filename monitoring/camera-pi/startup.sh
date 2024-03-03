#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd ~/projects/3dprinting/monitoring/camera-pi/src
sudo pip install -r requirements.txt
sudo python cleanup.py
sudo python app.py
cd /
