import json
import os
import shutil
from typing import Union

import requests
import requests.exceptions
import appdirs

from sugaroid.version import VERSION

ORG_URL = "https://raw.githubusercontent.com/sugaroidbot"


class Session:
    def __init__(self):
        self._has_internet = True
        self._local_data_path = os.path.join(
            appdirs.user_data_dir("sugaroid"), "datasets"
        )
        self._latest_version = VERSION
        self._check_internet_connection()

    def _check_internet_connection(self):
        """
        Checks the internet connection.
        :return:
        :rtype:
        """
        try:
            content = requests.get(
                f"{ORG_URL}/sugaroid/master/sugaroid/version.py"
            ).text
            version = content[content.find('"') : -1]
            self._latest_version = version
        except requests.exceptions.ConnectionError:
            self._has_internet = False

    def has_network_access(self) -> bool:
        return self._has_internet

    def is_latest(self) -> bool:
        """
        Checks if Sugaroid is at the latest version
        :return:
        :rtype:
        """
        return self._latest_version == VERSION

    def get_dataset(self, path: str) -> Union[str, dict]:
        """
        Gets the dataset as string or json
        :param path:
        :type path:
        :return:
        :rtype:
        """
        if not self._has_internet:
            return ""

        _local_path = os.path.sep.join(path.split("/"))
        _abs_local_path = os.path.join(self._local_data_path, _local_path)
        if os.path.exists(_abs_local_path):
            with open(_abs_local_path) as fp:
                return json.load(fp)
        if "hangman" in path:
            txt_api_endpoint = f"{ORG_URL}/datasets/main/datasets/{path}.txt"
            r = requests.get(txt_api_endpoint)
            if r.status_code != 200:
                raise RuntimeError(f"{r.status_code}, {r.reason}: {txt_api_endpoint}")
            return r.text

        json_api_endpoint = f"{ORG_URL}/datasets/main/datasets/{path}.json"
        r = requests.get(json_api_endpoint)
        if r.status_code != 200:
            raise RuntimeError(f"{r.status_code}, {r.reason}: {json_api_endpoint}")
        return r.json()

    def refresh(self):
        """
        Refresh the datasets and re-download the new ones
        :return:
        :rtype:
        """
        shutil.rmtree(self._local_data_path)
        os.makedirs(self._local_data_path, exist_ok=True)

        from sugaroid.brain.hangman.constants import WORDS

        WORDS.clear()
