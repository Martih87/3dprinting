#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd ~/projects/3dprinting/monitoring/camera-pi/src
sudo touch output.log
sudo chmod 777 output.log
sudo pip install -r requirements.txt
sudo python cleanup.py
sudo python app.py  > output.log &
cd /
