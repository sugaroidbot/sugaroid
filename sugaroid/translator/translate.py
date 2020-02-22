from googletrans import Translator


class Translate:
    def __init__(self):
        self.t = Translator()
        pass

    def render(self, args):
        return self.t.translate(args).text

    def process(self, args):
        raise NotImplementedError
