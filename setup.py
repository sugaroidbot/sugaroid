from setuptools import setup
import sys
import os
from os import path

setup(
    name='sugaroid',
    version="{}".format(0.1),
    description='sugaroid',
    license='GPL v3',
    author='srevinsaju',
    author_email="srevin03@gmail.com",
    packages=['sugaroid'],
    url="https://srevinsaju.github.io/guiscrcpy",
    download_url="https://github.com/srevinsaju/guiscrcpy/archive/master.zip",
    package_data={'sugaroid': ['*', '*.*', 'brain/*', 'reader/*', 'trainer/*', 'translator/*', 'web/*', 'cli/*',
                               'platform/*', 'tts/*', 'config/*', 'google/*'],
                  '.': [".git/info/*"]
                  },
    include_package_data=True,
    install_requires=['chatterbot', 'googletrans'],

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
