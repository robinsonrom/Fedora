#!/bin/python
# -*- coding: utf-8 -*-

import requests

CITY = "4833387" # City ID
# API_KEY = "d179235a378d7005b408ae177c4e3aa0"
API_KEY = "65534e6ea3ecd9894aa1eadfea671f40"
UNITS = "Imperial"
UNIT_KEY = "F"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=imperial&lang=en".format(CITY, API_KEY))
try:
    # HTTP CODE = OK
    if REQ.status_code == 200:
        CURRENT = REQ.json()["weather"][0]["description"].capitalize()
        TEMP = int(float(REQ.json()["main"]["temp"]))
        HUMIDITY = int(float(REQ.json()["main"]["humidity"]))
        print("{} | {} °{} | {}% Humidity".format(CURRENT, TEMP, UNIT_KEY, HUMIDITY))
    else:
        print("Error: BAD HTTP STATUS CODE " + str(REQ.status_code))
except (ValueError, IOError):
    print("Error: Unable print the data")

