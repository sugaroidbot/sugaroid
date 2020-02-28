from setuptools import setup
import sys
import os
from os import path

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sugaroid',
    version="{}".format('0.2'),
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
                               'platform/*', 'tts/*', 'config/*', 'google/*', 'qt/*', 'game/*'],
                  '.': [".git/info/*"]
                  },
    include_package_data=True,
    install_requires=['chatterbot', 'googletrans', 'google', 'Django==3.0.3', 'chatterbot_corpus', 'pyjokes',
                      'scikit-learn', 'nltk', 'lxml', 'PyQt5'],

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
