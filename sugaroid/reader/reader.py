import json
import os

import mistletoe
import wget
from bs4 import BeautifulSoup


class MarkdownReader:
    """
    Converts a Markdown into HTML for parsable output
    """

    def __init__(self, file_path):
        self.file = self.check_file_path(file_path)
        self.html = self.read_markdown(self.file)
        self.soup = self.init_soup(self.html)

        self.headings = []
        self.content = []
        pass

    @staticmethod
    def check_file_path(file_path):
        if os.path.exists(os.path.abspath(file_path)):
            return os.path.abspath(file_path)
        else:
            return FileNotFoundError("The specified file cannot be found")

    def get_headings(self):
        pass

    def get_parsed_content(self):
        headings = []
        content = []
        for i in self.soup.find_all():
            if i.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                headings.append(i.get_text())
                content.append(i.get_text())
            elif i.name in ['p', 'a', 'code']:
                content.append(i.get_text())
        return headings, content

    def get_content(self):
        return self.soup.find_all()

    @staticmethod
    def init_soup(html):
        return BeautifulSoup(html, 'html.parser')

    @staticmethod
    def read(file_path):
        contents = []
        with open(file_path, 'r') as r:
            contents.append(r.read().strip())
        return contents

    @staticmethod
    def read_markdown(path_to_md):
        with open(path_to_md, 'r') as r:
            contents = mistletoe.markdown(r)
        return contents


READ_FILES = dict()

files = {}


def main():
    with open('scrawl.json', 'r') as r:
        files = json.load(r)

    sugar_files = files['sugar']
    try:
        os.makedirs('scrawled')
    except FileExistsError:
        pass
    for i in sugar_files:
        wget.download('https://raw.githubusercontent.com/sugarlabs/{}'
                      .format(i), os.path.join('scrawled', i.split('/')[-1]))
    for markdown_file in os.listdir(os.path.abspath('scrawled')):
        READ_FILES[markdown_file] = MarkdownReader(
            os.path.join('scrawled', markdown_file))

    scrawled = dict()
    for markdown_file in READ_FILES:
        scrawled[markdown_file] = READ_FILES[markdown_file].get_parsed_content()

    with open('scrawled.py', 'w') as w:
        w.write("SCRAWLED = {}".format(scrawled))


if __name__ == '__main__':
    main()
