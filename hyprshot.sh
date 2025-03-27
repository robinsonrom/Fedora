#!/bin/bash

name=$(date +%s)
hyprshot -m output -o ~/Pictures/screenshots/ -f $name.png
notify-send "Screenshot saved as ${name}.png."
