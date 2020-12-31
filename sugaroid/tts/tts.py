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
            gTTS('Let me try that,').save(os.path.join(
                self.tts_dir, 'let_me_try_that.mp3'))
        if not os.path.exists(os.path.join(self.tts_dir, 'why_do_you_think.mp3')):
            gTTS('Why do you think').save(os.path.join(
                self.tts_dir, 'why_do_you_think.mp3'))
        if not os.path.exists(os.path.join(self.tts_dir, 'did_you_mean_any_of_these.mp3')):
            gTTS('Did you mean any of these?').save(os.path.join(
                self.tts_dir, 'did_you_mean_any_of_these.mp3'))

    def speak(self, args):
        let_me = False
        why_do = False
        did_you_mean = False
        if args.lower().startswith('let me try that'):
            text = args.lower().lstrip('let me try that')
            print("TTS: ", text)
            let_me = True
        elif args.lower().startswith('why do you think'):
            text = args.lower().lstrip('why do you think')
            why_do = True
        elif 'ok ok' in args.lower():
            text = 'ok ok'
        elif 'did you mean any of' in args.lower():
            did_you_mean = True
            text = 'Did you mean any of these?'
        else:
            text = args
        if len(text) > 50:
            text = text.split('.')[0]
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
