__version__ = '0.1'


import json
import os
import time
from sugaroid.config.config import ConfigManager

class SugaroidTrainer:
    def __init__(self):

        print("Sugaroid Trainer v{}".format(__version__))

    def train(self, trainer):
        with open('trainer.json', 'r') as r:
            data = json.load(r)

        for i in data:
            trainer.train(data[i])

    def modify(self):
        pass

    def prompt_cli(self):
        a = input("trainer @>")
        if a == "Q" or a == 'q':
            return False
        return a

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
