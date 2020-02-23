__version__ = '0.1'


import json
import os
import time
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
