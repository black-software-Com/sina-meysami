#!/bin/sh
#

if [[ "$(id -u)" -ne 0 ]];
then
  echo "
Please, Run This Program as Root!
"
  exit
fi

function Main() {
    printf '\033]2;Sina Meysami\a'
    clear
    echo "---[ Sina Meysami ]---"
    sleep 2
    chmod +x main.py
    apt install python
    apt install python3
    apt install python3-pip
    pip3 install --upgrade pip
    pip3 install -r requirements.txt
    sleep 1
    echo "
Finish...
"
    sleep 0.5
    echo "
Usage:
      python main.py
    "
    sleep 0.5
    exit
}
Main