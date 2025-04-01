#!/bin/python
# -*- coding: utf-8 -*-

import requests
import json

icons_list = {
    "01d": "", # Clear sky day.
    "01n": "望", # Clear sky night.
    "02d": "", # Few clouds day.
    "02n": " ", # Few clouds night.
    "03d": " ", # Scattered clouds day.
    "03n": " ", # Scattered clouds night.
    "04d": " ", # Broken clouds day.
    "04n": " ", # Broken clouds night.
    "09d": "歹", # Shower rain day.
    "09n": "歹", # Shower rain night.
    "10d": " ", # Rain day.
    "10n": " ", # Rain night
    "11d": " ", # Thunderstorm day.
    "11n": " ", # Thunderstorm night
    "13d": " ", # Snow day. Non-Snowflake alternative:  
    "13n": " ", # Snow night. Non-Snowflake alternative: 
    "50d": " ", # Mist day.
    "50n": " ", # Mist night.
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
        DESC = REQ.json()["weather"][0]["description"] 
        TEMP = int(float(REQ.json()["main"]["temp"]))
        HUMIDITY = int(float(REQ.json()["main"]["humidity"]))
        WINDSPEED = int(float(REQ.json()["wind"]["speed"]))
        FEELS = int(float(REQ.json()["main"]["feels_like"]))
        PRESSURE = int(float(REQ.json()["main"]["pressure"]))
        HIGH = int(float(REQ.json()["main"]["temp_max"]))
        LOW = int(float(REQ.json()["main"]["temp_min"]))
        print("{}   {}   {}°{}   Humidity {}%".format(DESC, CURRENT, TEMP, UNIT_KEY, HUMIDITY))
        print("Feels Like: {}°{}   Pressure: {} hPa".format(FEELS, UNIT_KEY, PRESSURE))
        print("Wind Speed: {} mph".format(WINDSPEED))
        print("Today's High: {}°{}    Today's Low: {}°{}\n".format(LOW, UNIT_KEY, HIGH, UNIT_KEY))
        print("          ~~~~~~~~~~~ ")
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")
