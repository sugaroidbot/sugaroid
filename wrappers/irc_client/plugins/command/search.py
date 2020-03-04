#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A plugin for Autobot that returns a search result"""

import configparser
import re
import json
from urllib.parse import quote_plus
from requests import get
from bs4 import BeautifulSoup

def fetch(url, url_params):
    hdr = {'User-Agent': 'Autobot/1.0 (+https://github.com/meskarune/autobot)',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.9',
           'Connection': 'keep-alive'}
    return get(url, headers=hdr, params=url_params)

def ddg(search):
    """Search duck duck go and return the first url from the restuls"""
    if search[0].startswith("!"):
        try:
            ddapi_params = {"format" : "json", "no_html" : "1", "no_redirect": "1", "q": search}
            results = fetch("http://api.duckduckgo.com", ddapi_params).json()
            if results['Redirect']:
                link = results['Redirect']
            else:
                link = "None"
        except:
            return
    else:
        try:
            ddparams = {"kl": "us-en", "k1": "-1", "kd": "-1", "kp": "1", "t": "Autobot", "q": search}
            site = fetch("http://duckduckgo.com/lite", ddparams)
        except:
            return
        try:
            parsed = BeautifulSoup(site.text, "html.parser")
        except:
            return
        try:
            link = parsed.findAll('a', {'class': 'result-link'})[0]['href']
        except:
            return
    if len(link) > 250:
        return "{0}…".format(link[0:250])
    else:
        return link

def wiki(search):
    """Search Wikipedia and return a short description and Link to the result"""
    try:
        wikiparams = {"action": "opensearch", "search": search, "format": "json"}
        results = fetch("https://en.wikipedia.org/w/api.php", wikiparams).json()
        link = results[3][0]
        description = results[2][0]
        if description:
            if len(description) > 250:
                data = "{0}… - {1}".format(description[0:250],link)
            else:
                data = "{0} - {1}".format(description,link)
        else:
            data = link
    except:
        return
    return data

def alwiki(search):
    """Search the arch linux wiki and return a Link to the result"""
    try:
        wikiparams = {"action": "opensearch", "search": search, "format": "json"}
        results = fetch("https://wiki.archlinux.org/api.php", wikiparams).json()
        description = results[1][0]
        link = results[3][0]
        if description:
            if len(description) > 250:
                data = "{0}… - {1}".format(description[0:250],link)
            else:
                data = "{0} - {1}".format(description,link)
        else:
            data = link
    except:
        return
    return data

def github(search):
    """Search Github and return url"""
    try:
        results = fetch("https://api.github.com/search/repositories", {"q": search}).json()
        description = results['items'][0]['description']
        link = results['items'][0]['html_url']
        if description:
            if len(description) > 250:
                data = "{0}… - {1}".format(description[0:250],link)
            else:
                data = "{0} - {1}".format(description,link)
        else:
            data = link
    except:
        return
    return data

def ud(search):
    """Search Urban Dictionary and return a deffinition and a Link to the result"""
    try:
        results = fetch("https://api.urbandictionary.com/v0/define", {"term": search}).json()
        definition = results['list'][0]['definition']
        description = definition.strip().translate(str.maketrans('','','\r\n'))
        link = results['list'][0]['permalink']
        if description:
            if len(description) > 250:
                data = "{0}… - {1}".format(description[0:250],link)
            else:
                data = "{0} - {1}".format(description,link)
        else:
            data = link
    except:
        return
    return data

def imdb(search):
    """Search for movie information"""
    config = configparser.ConfigParser()
    config.read("plugins/command/search.conf")
    try:
        oparams = {"apikey": config.get("Key", "api_key_omdb"), "t": search}
        results = fetch("http://www.omdbapi.com/", oparams).json()
        title = results['Title']
        year = results['Year']
        description = results['Plot']
        movID = results['imdbID']
        if description:
            if len(description) > 250:
                reply = "{0} ({1}): {2}… - https://www.imdb.com/title/{3}/".format(title, year, description[0:250], movID)
            else:
                reply = "{0} ({1}): {2} - https://www.imdb.com/title/{3}/".format(title, year, description, movID)
        else:
            reply = "{0} ({1}) - https://www.imdb.com/title/{3}/".format(title, year, movID)
    except:
        return
    return reply
