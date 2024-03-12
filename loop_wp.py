#!/usr/bin/python3

import time
from os import system as cmd
delay = 60
while True:
	command = "feh --randomize --bg-fill ${HOME}/pictures/wallpapers/"
	cmd(command)
	time.sleep(delay)
