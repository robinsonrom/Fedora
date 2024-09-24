#!/bin/bash

name=$(date +%s)
magick import -window root ~/Pictures/screenshots/${name}.png
notify-send "Screenshot saved as ${name}.png."