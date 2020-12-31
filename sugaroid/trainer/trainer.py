"""
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
__version__ = '0.1'


import json
import os
import time
from colorama import Fore
from sugaroid.config.config import ConfigManager


class SugaroidTrainer:
    def __init__(self):
        self.cfgmgr = None
        print("Sugaroid Trainer v{}".format(__version__))

    def train(self, trainer):
        print('Initializing trainer')
        self.cfgmgr = ConfigManager()

        data = self.cfgmgr.get_config()
        il = []
        for i in data:
            il.append(i)
            trainer.train(data[i])
        with open(os.path.join(self.cfgmgr.get_cfgpath(), 'data.json'), 'w') as w:
            json.dump({"il": il}, w)

    def modify(self):
        pass

    @staticmethod
    def prompt_cli():
        try:
            a = input("trainer @>")
            if a == "Q" or a == 'q':
                return False
            return a
        except KeyboardInterrupt:
            return False

    def reset(self):
        self.cfgmgr.reset_config()

    def write(self):
        self.cfgmgr.update_config(self.data)
        self.cfgmgr.write_file()

    def trainer_init(self):
        self.cfgmgr = ConfigManager()
        self.data = self.cfgmgr.get_config()
        self.trainer = []

    def trainer_cli(self):
        while True:
            conversation = self.prompt_cli()
            if conversation:
                self.trainer.append(conversation)
            else:
                break
        self.data["{}".format(time.time())] = self.trainer
        self.write()


def main():
    st = SugaroidTrainer()
    st.trainer_init()
    st.trainer_cli()


if __name__ == "__main__":
    main()
