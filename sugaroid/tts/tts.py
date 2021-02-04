"""
Sugaroid Text2Speech Adapter.

Sugaroid has the feature of enabling text-to-voice for 
messages coming from sugaroid. Sugaroid uses ``gTTS`` to 
convert ``SugaroidStatement`` to audio file, which is then
played through an audio device using ``playsound.playsound``
"""

import os

from gtts import gTTS
from playsound import playsound

from sugaroid.config.config import ConfigManager


class Text2Speech:
    def __init__(self):
        """
        Initializes the Text2Speech adapter for sugaroid

        The ``Text2Speech`` adapter includes a smart algorithm
        to automatically reduce downloads and cache messages
        so that they can be reused on every outgoing message
        from sugaroid. Sugaroid uses Google Speech API to
        convert text messages into audio files. The Speech
        materials ``(*.mp3)`` are stored in the default
        configuration as provided by the ``ConfigManager``

        Text2Speech Adapter can be used as

            >>> t2s = Text2Speech()
            >>> t2s.speak("Hello, I am Sugaroid")

        """

        self.cfgmgr = ConfigManager()
        if not os.path.exists(os.path.join(self.cfgmgr.get_cfgpath(), "tts")):
            os.makedirs(os.path.join(self.cfgmgr.get_cfgpath(), "tts"))
        self.tts_dir = os.path.join(self.cfgmgr.get_cfgpath(), "tts")
        if not os.path.exists(os.path.join(self.tts_dir, "let_me_try_that.mp3")):
            gTTS("Let me try that,").save(
                os.path.join(self.tts_dir, "let_me_try_that.mp3")
            )
        if not os.path.exists(os.path.join(self.tts_dir, "why_do_you_think.mp3")):
            gTTS("Why do you think").save(
                os.path.join(self.tts_dir, "why_do_you_think.mp3")
            )
        if not os.path.exists(
            os.path.join(self.tts_dir, "did_you_mean_any_of_these.mp3")
        ):
            gTTS("Did you mean any of these?").save(
                os.path.join(self.tts_dir, "did_you_mean_any_of_these.mp3")
            )

    def speak(self, args: str):
        """
        Speaks a statement using gTTS or plays a downloaded file
        if the ``args`` matches the downloaded files name

        :param args: The text to speak
        :type args: str
        """
        let_me = False
        why_do = False
        did_you_mean = False
        if args.lower().startswith("let me try that"):
            text = args.lower().lstrip("let me try that")
            print("TTS: ", text)
            let_me = True
        elif args.lower().startswith("why do you think"):
            text = args.lower().lstrip("why do you think")
            why_do = True
        elif "ok ok" in args.lower():
            text = "ok ok"
        elif "did you mean any of" in args.lower():
            did_you_mean = True
            text = "Did you mean any of these?"
        else:
            text = args
        if len(text) > 50:
            text = text.split(".")[0]
        processed = text.lower().replace(" ", "_") + ".mp3"
        path = os.path.join(self.tts_dir, processed)
        if os.path.exists(path):
            pass
        else:
            en = gTTS(text)
            en.save(path)
        if why_do:
            playsound(os.path.join(self.tts_dir, "why_do_you_think.mp3"))
        if let_me:
            playsound(os.path.join(self.tts_dir, "let_me_try_that.mp3"))
        playsound(path)
