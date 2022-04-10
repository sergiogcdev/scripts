#!/usr/bin/python3

import time, random, signal, subprocess
from os import system as cmd
from os import listdir, kill

def run_swaybg():
    delay = 100
    devnull = open('/dev/null', 'w')
    random_file = random.choice(listdir("/home/sergio/Pictures/wallpapers/"))
    command1 = "swaybg --image /home/sergio/Pictures/wallpapers/" + random_file + " --mode fill --output eDP-1"
    command2 = "swaybg --image /home/sergio/Pictures/wallpapers/" + random_file + " --mode fill --output HDMI-A-1"
    p1 = subprocess.Popen(command1, stdout=devnull, shell=True)
    p2 = subprocess.Popen(command2, stdout=devnull, shell=True)
    time.sleep(delay)
    pid1 = p1.pid
    pid2 = p2.pid
    kill(pid1, signal.SIGINT)
    kill(pid2, signal.SIGINT)

def main():
    while True:
        run_swaybg()

if __name__ == '__main__':
    main()
