import re
import requests
from swaglyrics.cli import stripper, get_lyrics
from chatterbot.logic import LogicAdapter
from sugaroid.sugaroid import SugaroidStatement
from sugaroid.brain.ooo import Emotion
from sugaroid.brain.preprocessors import normalize

backend_url = "https://api.swaglyrics.dev"


class LyricsNotFound(Exception):
    """
    Exception raised when the lyrics has not been found in Genius through
    Swaglyrics
    """
    pass


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
