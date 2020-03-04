#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A plugin for Autobot that checks if a site is up and returns the status code"""


from requests import get

def isup(website):
    """Make a request to the site and pull the statue code"""
    messages = {
        "1": "The webserver hasn't sent a final response, status {0}",
        "2": "The website is up status {0}",
        "3": "The website is up with a {0} redirect",
        "4": "Client error, webserver returned status {0}",
        "5": "Server returning error {0}"}

    if website.startswith("http://") or website.startswith("https://"):
        address = website
    else:
        address = "http://{0}".format(website)
    try:
        getsite = get(address)
        getstatus = str(getsite.status_code)
        message = messages.get(getstatus[0])
        return message.format(getstatus)
    except:
        return "The website is currently down"
