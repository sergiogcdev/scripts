#!/usr/bin/python3

import subprocess

def get_password_internet():
    output = subprocess.getoutput("pass show Neomutt")
    return output

def get_password_work():
    output = subprocess.getoutput("pass show NeomuttWork")
    return output
