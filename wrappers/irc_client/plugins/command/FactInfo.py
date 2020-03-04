#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A plugin for Autobot that stores keyword/response pairs and returns them"""

import sys
import json
import os.path

class FactInfo(object):
    def __init__(self):
        """Create the db if it doesn't exist"""
        self.schema = {"admins":[],"factinfo":{}}
        self.db = "data/factinfo.json"
        if os.path.isfile(self.db) is False:
            """create the json file"""
            jsonData = self.schema
            with open(self.db, 'w') as jsonFile:
                json.dump(jsonData,jsonFile, sort_keys = True,
                          indent = 4, ensure_ascii=False)
        try:
            with open(self.db, encoding='utf-8') as jsonFile:
                self.results = json.loads(jsonFile.read())
        except ValueError as err:
            sys.stderr.write("Error with factinfo.json: {0}\n".format(err))
            return
        except:
            return
    def fcaddadmin(self, nick):
        """Add nick to admins: list"""

    def fcaddkey(self, keyword,response):
        """Add a factinfo entry"""

    def fcget(self, keyword, user):
        """Pull factinfo response from the database"""
        try:
            response = self.results['factinfo'][keyword]
            return response.format(user)
        except:
            return False
