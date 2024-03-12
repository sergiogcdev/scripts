#!/bin/bash
wpa_supplicant -B -Dnl80211 -i wlp3s0 -c /etc/wpa_supplicant/wpa_supplicant.conf
ifconfig wlp3s0 up
dhclient wlp3s0
