#!/usr/bin/env bash
# Author: Suchith Sridhar
# Website: https://suchicodes.com/
#
# This script is used to manage power based controls on Hyprland
# These are operations like shutdown, lock, and logout.
# 
# Before performing some of these operations we handle the closing of apps.
# If there are apps that can't be closed without losing data, then the power operation
# is cancelled and a notification about the cause of the cancellation is sent.

function close_apps() {
    BRAVE=$(hyprctl clients | grep "class: brave-browser" | wc -l)
    CHROMIUM=$(hyprctl clients | grep "class: brave-browser" | wc -l)
    FIREFOX=$(hyprctl clients | grep "class: firefox" | wc -l)

    if [ "$BRAVE" -gt "1" ]; then
        notify-send "power controls" "Brave multiple windows open"
        exit 1
    elif [ "$CHROMIUM" -gt "1" ]; then
        notify-send "power controls" "Chromium multiple windows open"
        exit 1
    elif [ "$FIREFOX" -gt "1" ]; then
        notify-send "power controls" "Firefox multiple windows open"
        exit 1
    fi

    sleep 3

    # close all client windows
    # required for graceful exit since many apps aren't good SIGNAL citizens
    HYPRCMDS=$(hyprctl -j clients | jq -j '.[] | "dispatch closewindow address:\(.address); "')
    hyprctl --batch "$HYPRCMDS" >> /tmp/hypr/hyprexitwithgrace.log 2>&1

    notify-send "power controls" "Closing Applications..."

    sleep 2

    COUNT=$(hyprctl clients | grep "class:" | wc -l)
    if [ "$COUNT" -eq "0" ]; then
        notify-send "power controls" "Closed Applications."
        return
    else
        notify-send "power controls" "Some apps didn't close. Not shutting down."
        exit 1
    fi
}

function lock_screen() {
    swaylock --clock --indicator --timestr="%I:%M %p" --datestr="%Y/%m/%d" --image ~/.wallpaper.png --ring-color=0e5db2 --key-hl-color=3b97f9 --text-color=ffffff --inside-color=000000dd &
}

case "$1" in
        shutdown)
                close_apps
                systemctl poweroff
             ;;
        reboot | restart)
                close_apps
                systemctl reboot
            ;;

        suspend)
            lock_screen
            sleep 3
            systemctl suspend
            ;;

        hibernate)
            lock_screen
            systemctl hibernate
            ;;

        logout)
            close_apps
            hyprctl dispatch exit
            ;;

        lock)
            lock_screen
            ;;

        close)
            close_apps
            ;;
        *)
            echo $"Usage: $0 {shutdown|reboot|suspend|hibernate|logout|lock|close}"
            exit 1
esac
