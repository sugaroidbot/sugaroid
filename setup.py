#!/usr/bin/env python3
"""
MIT License

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

from setuptools import setup
import os

try:
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(
        os.path.join(this_directory, 'README.md'),
        encoding='utf-8'
    ) as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = \
        "Sugaroid Bot by @srevinsaju"

requirements = ['googletrans', 'google', 'Django', 'pyjokes', 'scikit-learn',
                'nltk', 'lxml', 'pyinflect', 'newsapi-python', 'wikipedia-API',
                'pyspellchecker', 'python-dotenv', 'psutil', 'emoji',
                'akinator.py', 'CurrencyConverter', 'colorama']


setup(
    name='sugaroid',
    version='v0.11.2',
    description='Open Source Natural Language Processing Bot.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author='srevinsaju',
    author_email="srevin03@gmail.com",
    packages=['sugaroid', 'sugaroid.brain', 'sugaroid.gui', 'sugaroid.cli',
              'sugaroid.config', 'sugaroid.reader', 'sugaroid.config',
              'sugaroid.game', 'sugaroid.web', 'sugaroid.trivia',
              'sugaroid.platform', 'sugaroid.google', 'sugaroid.translator',
              'sugaroid.tts', 'sugaroid.trainer', 'sugaroid.backend'],
    url="https://srevinsaju.github.io/sugaroid",
    download_url="https://github.com/srevinsaju/sugaroid/archive/master.zip",
    package_data={'sugaroid': ['data/*', 'gui/ui/*']},  # noqa: E501
    include_package_data=True,
    install_requires=requirements,
    entry_points={'console_scripts': ['sugaroid = sugaroid.sugaroid:main']},  # noqa: E501
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
    ],
)
