__version__ = '0.1'


import json
import time


class SugaroidTrainer:
    def __init__(self):
        self.data = {}
        print("Sugaroid Trainer v{}".format(__version__))

    def train(self, trainer):
        with open('trainer.json', 'r') as r:
            data = json.load(r)

        for i in data:
            trainer.train(data[i])

    def modify(self):
        pass

    def prompt(self):
        a = input("trainer @>")
        if a == "Q" or a == 'q':
            return False
        return a

    def read(self):
        with open('trainer.json', 'r') as r:
            self.data = json.loads(r.read())

    def write(self):
        with open('trainer.json', 'w+') as w:
            json.dump(self.data, w)

    def trainer_init(self):
        self.read()
        self.trainer = []

    def trainer_cli(self):
        while True:
            conversation = self.prompt()
            if conversation:
                self.trainer.append(conversation)
            else:
                break
        self.data["{}".format(time.time())] = self.trainer



if __name__ == "__main__":
    st = SugaroidTrainer()
    st.trainer_init()
    st.trainer_cli()