"""
MIT License

Sugaroid Artificial Inteligence
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
import sys
import logging
import time
from PyQt5 import QtCore, Qt, QtGui
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
from emoji import emojize

from sugaroid.brain.constants import emotion_mapping as emotion
from sugaroid.brain.ooo import Emotion
from sugaroid.gui.ui.main import Ui_MainWindow
import threading


"""
class SleepRequests:
    def __init__(self, parent):
        self.parent = parent
        self.sleeping = True

    def set_sleeping(self, boo):
        self.sleeping = boo

    def run(self):
        while self.sleeping:
            if self.parent.sleep <= 20:
                time.sleep(1)
                self.parent.sleep += 1

            else:
                self.parent.label.setPixmap(QPixmap(":/home/sugaroid_sleep.png"))
                break
"""


class AudioRequests:
    def __init__(self, parent, ress):

        self.parent = parent
        self.response = ress

    def run(self):
        self.parent.parent.tts.speak(self.response)


class EmotionRequests(QThread):
    def __init__(self, parent, emo):
        QThread.__init__(self, parent)
        self.parent = parent
        self.emotion = emo

    def run(self):
        self.parent.label.setPixmap(
            QPixmap(":/home/{}.png".format(emotion[self.emotion])))
        time.sleep(5)
        self.parent.label.setPixmap(QPixmap(":/home/sugaroid.png"))


class BotRequests(QThread):
    def __init__(self, parent):
        QThread.__init__(self, parent)
        self.parent = parent

    def run(self):
        text = self.parent.chatbox.text()
        self.parent.conv.addItem("you: {}".format(text))
        self.parent.chatbox.setText("")
        self.parent.conv.scrollToBottom()
        response = self.parent.parent.parse(text)

        self.parent.conv.addItem("sugaroid: {}".format(emojize(str(response))))
        time.sleep(0.1)

        if response.emotion != 0:
            self.parent.label.setPixmap(
                QPixmap(":/home/{}.png".format(emotion[response.emotion])))
            self.parent.conv.scrollToBottom()
            time.sleep(5)

        self.parent.label.setPixmap(QPixmap(":/home/sugaroid.png"))
        self.parent.conv.scrollToBottom()

        if self.parent.parent.audio:
            aud = AudioRequests(self.parent, str(response))
            y = threading.Thread(target=aud.run)
            y.start()


class InterfaceSugaroidQt(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.sleep = 0

        self.sleep_enabled = True
        if parent is None:
            from sugaroid.sugaroid import Sugaroid
            sg = Sugaroid()
            self.parent = sg
        else:
            self.parent = parent

    def init(self):
        self.push.pressed.connect(self.refresh)
        self.chatbox.returnPressed.connect(self.refresh)
        self.conv.clear()
        self.show()

        self.chatbox.setFocus()

    def refresh(self):
        # if self.sleep_enabled:
        #    if self.sl_thread.is_alive():
        #        self.sl.set_sleeping(False)
        #        self.sl_thread.join()
        #        print("THREAD IS SLEEPING", not self.sl_thread.is_alive())

        # self.sleep = 0
        # if self.sleep_enabled:
        #    if not self.sl_thread.is_alive():
        #        self.sl_thread = threading.Thread(target=self.sl.run)
        #        self.sl_thread.start()

        if str(self.chatbox.text()).isspace():
            return
        movie = QtGui.QMovie(":/home/sugaroid_thinking3.gif")
        self.label.setMovie(movie)
        movie.start()

        bot = BotRequests(self)
        bot.start()
