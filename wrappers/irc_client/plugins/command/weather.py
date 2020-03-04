#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A plugin for Autobot that gives the weather"""

import configparser
import json
from requests import get


def parseweather(data):
    icon_list = {
        "01": "☀",
        "02": "🌤",
        "03": "🌥",
        "04": "☁",
        "09": "🌧",
        "10": "🌦",
        "11": "🌩",
        "13": "🌨",
        "50": "🌫",
    }
    weather = {
        "location"    : data["name"],
        "conditions"  : data["weather"][0]["main"],
        "temperature" : round(float(data["main"]["temp"])),
        "humidity"    : round(float(data["main"]["humidity"])),
        "icon"        : icon_list.get(data["weather"][0]["icon"][:2],""),
        "windspeed"   : round(data["wind"]["speed"])
        }
    if data["sys"]["country"] == "US":
        weather.update( {
            "scale" : "°F",
            "speed" : "mph"
        })
    else:
        weather.update( {
            "scale" : "°C",
            "speed" : "kph"
        })
    return weather

def parsegeocode(geo):
    r = geo["results"][0]["locations"][0]
    location =  {
            "lat" : r["latLng"]["lat"],
            "lon" : r["latLng"]["lng"]
    }
    if r["adminArea1"] == "US":
        location["units"] = "imperial"
    else:
        location["units"] = "metric"
    return location

def fetch(url, params):
    return get(url, params = params).json()

def getweather(location):
    """Get wearther and return the result"""
    config = configparser.ConfigParser()
    config.read("plugins/command/weather.conf")
    try:
        position = parsegeocode(fetch("http://open.mapquestapi.com/geocoding/v1/address", params = {
            "key" : config.get("Key", "api_key_geocode"),
            "location" : location
        }))
    except:
        return "Error getting location data"
    position.update( { "appid" : config.get("Key", "api_key_weather") } )
    try:
        weather = parseweather(fetch("https://api.openweathermap.org/data/2.5/weather", params = position))
    except:
        return "Error getting weather data"
    template = "The current weather for {location} is {temperature}{scale} {icon} {conditions}, {humidity}% humidity with {windspeed}{speed} wind"
    return template.format(**weather)
