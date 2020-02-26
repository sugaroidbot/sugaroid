import os

from gtts import gTTS
from playsound import playsound

from sugaroid.config.config import ConfigManager


class Text2Speech:
    def __init__(self):
        self.cfgmgr = ConfigManager()
        if not os.path.exists(os.path.join(self.cfgmgr.get_cfgpath(), 'tts')):
            os.makedirs(os.path.join(self.cfgmgr.get_cfgpath(), 'tts'))
        self.tts_dir = os.path.join(self.cfgmgr.get_cfgpath(), 'tts')
        if not os.path.exists(os.path.join(self.tts_dir, 'let_me_try_that.mp3')):
            gTTS('Let me try that,').save(os.path.join(self.tts_dir, 'let_me_try_that.mp3'))
        if not os.path.exists(os.path.join(self.tts_dir, 'why_do_you_think.mp3')):
            gTTS('Why do you think').save(os.path.join(self.tts_dir, 'why_do_you_think.mp3'))

    def speak(self, args):
        let_me = False
        why_do = False
        if args.lower().startswith('let me try that'):
            text = args.lower().lstrip('let me try that')
            print("TTS: ", text)
            let_me = True
        elif args.lower().startswith('why do you think'):
            text = args.lower().lstrip('why do you think')
            why_do = True
        elif 'ok' in args.lower():
            text = 'ok ok'
        else:
            text = args

        processed = text.lower().replace(' ', '_') + '.mp3'
        path = os.path.join(self.tts_dir, processed)
        if os.path.exists(path):
            pass
        else:
            en = gTTS(text)
            en.save(path)
        if why_do:
            playsound(os.path.join(self.tts_dir, 'why_do_you_think.mp3'))
        if let_me:
            playsound(os.path.join(self.tts_dir, 'let_me_try_that.mp3'))
        playsound(path)