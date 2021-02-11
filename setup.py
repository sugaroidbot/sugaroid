#!/usr/bin/env python3
from setuptools import setup
import os

from sugaroid.version import VERSION

try:
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Sugaroid Bot by @srevinsaju"


def gen_version():
    """
    Generates a version from the available git repositories
    If git repository is not valid, fallback to __version__
    :return:
    """
    import git

    repo = git.Repo(search_parent_directories=True)
    ver = repo.git.describe("--tags")
    raw_version = ver.split("-")
    if len(raw_version) == 1:
        # Stable Release
        git_version = "{}".format(raw_version[0])
    elif len(raw_version) == 2:
        # Release Candidate
        git_version = "{major}.post{minor}".format(
            major=raw_version[0], minor=raw_version[1]
        )
    else:
        # Revision Dev
        git_version = "{major}.post{minor}.dev".format(
            major=raw_version[0], minor=raw_version[1]
        )
    return git_version


try:
    VERSION = gen_version()
except Exception as e:
    print("E: Could not git describe --tags")
    print(f"Fallback to {VERSION}")


requirements = [
    "googletrans",
    "google",
    "Django",
    "pyjokes",
    "scikit-learn",
    "coloredlogs",
    "nltk",
    "lxml",
    "pyinflect",
    "newsapi-python",
    "wikipedia-API",
    "pyspellchecker",
    "swaglyrics",
    "python-dotenv",
    "psutil",
    "emoji",
    "akinator.py",
    "CurrencyConverter",
    "colorama",
    "gitpython",
]


setup(
    name="sugaroid",
    version=VERSION,
    description="Open Source Natural Language Processing Bot.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="srevinsaju",
    author_email="srevin03@gmail.com",
    packages=[
        "sugaroid",
        "sugaroid.brain",
        "sugaroid.gui",
        "sugaroid.cli",
        "sugaroid.config",
        "sugaroid.reader",
        "sugaroid.config",
        "sugaroid.core",
        "sugaroid.game",
        "sugaroid.web",
        "sugaroid.trivia",
        "sugaroid.platform",
        "sugaroid.google",
        "sugaroid.translator",
        "sugaroid.tts",
        "sugaroid.trainer",
        "sugaroid.backend",
    ],
    url="https://srevinsaju.github.io/sugaroid",
    download_url="https://github.com/srevinsaju/sugaroid/archive/master.zip",
    package_data={"sugaroid": ["data/*", "gui/ui/*"]},  # noqa: E501
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["sugaroid = sugaroid.sugaroid:main"]
    },  # noqa: E501
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
