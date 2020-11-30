#!/usr/bin/env python

from setuptools import setup

setup(
    name='autobot',
    version='1.0',
    description="A full featured irc logging bot with plugin support",
    author="Dolores Portalatin",
    author_email='hello@doloresportalatin.info',
    url='https://github.com/meskarune/autobot',
    packages=['autobot'],
    package_dir={'autobot': 'src'},
    install_requires=["irclib", "urllib3", "beautifulsoup4"],
    license="GPL3"
)
