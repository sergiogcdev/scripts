#!/usr/bin/python

import time
from os import system as cmd

# seconds = 0
delay = 60

while True:
	command = "feh --randomize --bg-fill /home/sergio/Pictures/blackarchwallpapers/"
	cmd(command)
	time.sleep(delay)
	# seconds += 60
