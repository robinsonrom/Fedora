#!/bin/python
# -*- coding: utf-8 -*-

import requests
import json

icons_list = {
    "01d": "", # Clear sky day.
    "01n": "望", # Clear sky night.
    "02d": "", # Few clouds day.
    "02n": "", # Few clouds night.
    "03d": "", # Scattered clouds day.
    "03n": "", # Scattered clouds night.
    "04d": "", # Broken clouds day.
    "04n": "", # Broken clouds night.
    "09d": "歹", # Shower rain day.
    "09n": "歹", # Shower rain night.
    "10d": "", # Rain day.
    "10n": "", # Rain night
    "11d": "", # Thunderstorm day.
    "11n": "", # Thunderstorm night
    "13d": "", # Snow day. Snowflake alternative: 
    "13n": "", # Snow night. Snowflake alternative: 
    "50d": "", # Mist day.
    "50n": "", # Mist night.
}

CITY = "4833387" # City ID
# API_KEY = "d179235a378d7005b408ae177c4e3aa0"
API_KEY = "65534e6ea3ecd9894aa1eadfea671f40"
UNITS = "Imperial"
UNIT_KEY = "F"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=imperial&lang=en".format(CITY, API_KEY))
try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
        CURRENT = icons_list[REQ.json()["weather"][0]["icon"]]
        TEMP = int(float(REQ.json()["main"]["temp"]))
        HUMIDITY = int(float(REQ.json()["main"]["humidity"]))
        print(" {}  {}°{} | {}% Humidity".format(CURRENT, TEMP, UNIT_KEY, HUMIDITY))
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")
