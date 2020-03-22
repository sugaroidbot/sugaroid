#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A plugin for Autobot that announces the title for urls in IRC channels"""

import encodings
from requests import get
from requests import head
from urllib.parse import urlsplit
from bs4 import BeautifulSoup

def parse_url(link):
    """Say Website Title information in channel"""
    baseurl = '{uri.scheme}://{uri.netloc}'.format(uri=urlsplit(link))
    path = urlsplit(link).path
    query = '?{uri.query}'.format(uri=urlsplit(link))
    try:
        headers = {'Accept-Encoding': 'utf-8',
                   'User-Agent': 'Mozilla/5.0'}
        response = get(baseurl + path + query, headers=headers)
    except:
        return
    if response.headers["Content-Type"] and "text/html" in response.headers["Content-Type"]:
        try:
            URL = BeautifulSoup(response.text, "html.parser")
        except:
            return
        if not URL.title:
            return
        if URL.title.string is None:
            return
        if len(URL.title.string) > 250:
            title=URL.title.string[0:250] + '…'
        else:
            title=URL.title.string
        return title.replace('\n', ' ').strip() + " (" + urlsplit(link).netloc + ")"
    else:
        return
