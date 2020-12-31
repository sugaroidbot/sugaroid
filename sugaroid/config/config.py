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

MIT License

Sugaroid Artificial Inteligence
Chatbot Core
Copyright (c) 2020-2021 Srevin Saju
Copyright (c) 2021 The Sugaroid Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

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
            import nltk
            for lexicon in ['averaged_perceptron_tagger', 'stopwords', 'wordnet', 'vader_lexicon', 'punkt']:
                nltk.download(lexicon)
            self.write_file()
        self.read_file()

    def update_config(self, new_conf):
        self.config.update(new_conf)

    def reset_config(self):
        os.remove(os.path.join(self.get_cfgpath(), self.jsonfile))
        return True
