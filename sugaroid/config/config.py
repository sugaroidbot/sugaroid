"""
GUISCRCPY by srevinsaju
Get it on : https://github.com/srevinsaju/guiscrcpy
Licensed under GNU Public License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import json
import os


from sugaroid.platform import platform


class ConfigManager:
    def __init__(self, mode='w'):
        self.os = platform.System()
        self.cfgpath = self.os.cfgpath()
        self.paths = self.os.paths()
        self.config = {}
        self.jsonfile = 'sugaroid.trainer.json'
        self.check_file()

    def get_config(self):
        return self.config

    def get_cfgpath(self):
        return self.cfgpath

    def read_file(self):
        with open(os.path.join(self.cfgpath, self.jsonfile), 'r') as f:
            config = json.load(f)
        self.update_config(config)

    def write_file(self):
        with open(os.path.join(self.cfgpath, self.jsonfile), 'w') as f:
            json.dump(self.config, f, indent=4, sort_keys=True)

    def check_file(self):
        if not os.path.exists(self.cfgpath):
            os.mkdir(self.cfgpath)
        if not os.path.exists(os.path.join(self.cfgpath, self.jsonfile)):
            self.write_file()
        self.read_file()

    def update_config(self, new_conf):
        self.config.update(new_conf)

    def reset_config(self):
        os.remove(os.path.join(self.get_cfgpath(), self.jsonfile))
        return True