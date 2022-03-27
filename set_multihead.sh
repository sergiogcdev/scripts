#!/bin/sh
# xrandr --newmode "1920x1080"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync
# xrandr --addmode HDMI1 1920x1080
# xrandr --output HDMI1 --mode 1920x1080
xrandr \
--output eDP1 --primary --mode 1366x768 --pos 0x0 --rotate normal \ 
--output HDMI1 --mode 1920x1080 --right-of eDP1 --rotate normal
