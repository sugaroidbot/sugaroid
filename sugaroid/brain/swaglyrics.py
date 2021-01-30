"""
MIT License

Sugaroid Artificial Intelligence
Chatbot Core
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
import re
import requests
from swaglyrics.cli import stripper, get_lyrics
from chatterbot.logic import LogicAdapter
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize

backend_url = "https://api.swaglyrics.dev"


class LyricsNotFound(Exception):
    pass


def fetch(url, **kwargs):
    """
    Uses aiohttp to make http GET requests
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/84.0.4147.89 Safari/537.36"
    }
    req = requests.get(url, headers=headers, **kwargs)
    return req.text


class SwagLyricsAdapter(LogicAdapter):
    """
    Get the lyrics for a song using Swaglyrics
    """

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        self.normalized = str(statement).lower().strip().split()
        return "$ by" in str(statement) and "who" not in self.normalized

    def process(self, statement, additional_response_selection_parameters=None):
        if (
            self.normalized[0] == "get"
            and self.normalized[1] == "lyrics"
            and self.normalized[2] == "for"
        ):
            self.normalized[0:3] = []

        elif self.normalized[0] == "lyrics" and self.normalized[1] == "for":
            self.normalized[0:2] = []
        elif self.normalized[0] == "lyrics":
            self.normalized[0:1] = []

        stripped_message = " ".join(self.normalized).strip()
        try:
            song, artist = stripped_message.split("$ by")
        except Exception as e:
            selected_statement = SugaroidStatement(
                "Usage: _Hello $by Adele_ or " "_get lyrics for The Nights $by Avicii_",
                chatbot=True,
            )
            selected_statement.confidence = 1

            emotion = Emotion.lol
            selected_statement.emotion = emotion
            return selected_statement

        try:
            lyrics = get_lyrics(song, artist)
            if not lyrics or not lyrics.strip():
                raise LyricsNotFound

        except LyricsNotFound:
            lyrics = "I couldn't find the lyrics for '{}' by '{}'.".format(song, artist)

        selected_statement = SugaroidStatement(lyrics, chatbot=True)
        selected_statement.confidence = 1

        emotion = Emotion.lol
        selected_statement.emotion = emotion
        return selected_statement
