#!/usr/bin/python3
import subprocess
import time
# get openntpd server hour
while True:
    cmd = "timedatectl | awk '{ print $5 } ' | awk '$0 ~ \"00:00\"' | wc -l"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()[0]
    if '0' not in str(output):
        # get current system hour
        command = "date | awk '{print $5}'"
        ps = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout = ps.communicate()[0]
        # Send msg to display
        head = "Aviso hora\n"
        msg = 'Son las ' + str(stdout)
        subprocess.call(['notify-send', head, msg])
        time.sleep(5)
