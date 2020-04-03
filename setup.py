"""
MIT License

Sugaroid Artificial Intelligence
Chatbot Core
Copyright (c) 2020 Srevin Saju

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

from setuptools import setup


from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

REQUIREMENTS = []
DEPENDENCIES = []

with open('requirements.txt') as requirements:
    for requirement in requirements.readlines():
        if requirement.startswith('git+git://') or (requirement.startswith('https://')) \
                or (requirement.startswith('git+https://')):
            DEPENDENCIES.append(requirement)
        else:
            REQUIREMENTS.append(requirement)


def gen_version():
    import git

    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    ver = repo.git.describe("--tags")
    raw_version = ver.split('-')
    if len(raw_version) == 1:
        # Stable Release
        v = "{}".format(raw_version[0])
    elif len(raw_version) == 2:
        # Release Candidate
        v = "{major}.post{minor}".format(major=raw_version[0], minor=raw_version[1])
    else:
        # Revision Dev
        v = "{major}.post{minor}.dev".format(major=raw_version[0], minor=raw_version[1])

    return v

try:
    v = gen_version()
except Exception as e:
    print("WARNING: {}".format(e))
    v = "0.5.x"


setup(
    name='sugaroid',
    version="{}".format(v),
    description='sugaroid',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL v3',
    author='srevinsaju',
    author_email="srevin03@gmail.com",
    packages=['sugaroid'],
    url="https://srevinsaju.github.io/guiscrcpy",
    download_url="https://github.com/srevinsaju/guiscrcpy/archive/master.zip",
    package_data={'sugaroid': ['*', '*.*', 'brain/*', 'reader/*', 'trainer/*', 'translator/*', 'web/*', 'cli/*',
                               'platform/*', 'tts/*', 'config/*', 'google/*', 'qt/*', 'game/*', 'trivia/*', 'gui/*',
                               'gui/ui/*', 'data/*'],
                  '.': [".git/info/*"]
                  },
    include_package_data=True,
    install_requires=['GitPython' , 'googletrans', 'google', 'Django', 'pyjokes',
                      'scikit-learn', 'nltk', 'lxml', 'pyinflect'] + REQUIREMENTS,
    dependency_links=DEPENDENCIES,
    entry_points={
        'console_scripts': [
            'sugaroid = sugaroid.sugaroid:main',
        ]
    },
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.8',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'],
)
