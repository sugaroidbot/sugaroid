import json
import time


class Trainer:
    def __init__(self):
        print("Initializing Trainer")
        pass

    def train(self):
        pass

    def reinit(self):
        pass

    def prompt(self):
        pass

if __name__ == "__main__":
    trainer = []
    with open('trainer.json', 'r') as r:
        data = json.loads(r.read())
        print(data)

    while True:
        a = input("trainer @>")
        if a=="Q":
            break
        trainer.append(a)
    data["data {}".format(time.time())] =  trainer
    print(data)
    with open('trainer.json', 'w+') as w:
        json.dump(data, w)