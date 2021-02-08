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


class AudioRequests:
    """
    Allows sugaroid to simultanously run the
    Audio Requests thread as well as the Emotion Changing thread
    """

    def __init__(self, parent, ress):

        self.parent = parent
        self.response = ress

    def run(self):
        self.parent.parent.tts.speak(self.response)


class EmotionRequests(QThread):
    """
    Allows to run the emotion changing thread detached
    from the ``__main__`` thread
    """

    def __init__(self, parent, emo):
        QThread.__init__(self, parent)
        self.parent = parent
        self.emotion = emo

    def run(self):
        self.parent.label.setPixmap(
            QPixmap(":/home/{}.png".format(emotion[self.emotion]))
        )
        time.sleep(5)
        self.parent.label.setPixmap(QPixmap(":/home/sugaroid.png"))


class BotRequests(QThread):
    """
    Allows to ask sugaroid for responses on a detached thread
    from the main thread and also spawns ``AudioRequests`` and
    ``EmotionRequests`` if audio is enabled
    """

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
                QPixmap(":/home/{}.png".format(emotion[response.emotion]))
            )
            self.parent.conv.scrollToBottom()
            time.sleep(5)

        self.parent.label.setPixmap(QPixmap(":/home/sugaroid.png"))
        self.parent.conv.scrollToBottom()

        if self.parent.parent.audio:
            aud = AudioRequests(self.parent, str(response))
            y = threading.Thread(target=aud.run)
            y.start()


class InterfaceSugaroidQt(QMainWindow, Ui_MainWindow):
    """
    Prepares the user interface of Sugaroid on the main
    thread and spawns ``BotRequests`` thread on an adjacent
    thread
    """

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
        if str(self.chatbox.text()).isspace():
            return
        movie = QtGui.QMovie(":/home/sugaroid_thinking3.gif")
        self.label.setMovie(movie)
        movie.start()

        bot = BotRequests(self)
        bot.start()
