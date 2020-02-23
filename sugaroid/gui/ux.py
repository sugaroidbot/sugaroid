"""
sugaroid by srevinsaju
Get it on : https://github.com/srevinsaju/guiscrcpy
Licensed under GNU Public License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import logging
import time

from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow
from sugaroid.gui.ui.main import Ui_MainWindow

class BotRequests(QThread):


    def __init__(self, parent):
        QThread.__init__(self)
        self.parent = parent

    def __del__(self):
        self.wait()

    def run(self):
        text = self.parent.chatbox.text()
        self.parent.conv.addItem("you: {}".format(text))
        self.parent.chatbox.setText("")
        response = self.parent.parent.parse(text)
        self.parent.conv.addItem("sugaroid: {}".format(str(response)))
        self.parent:0.conv.scrollToBottom()


class InterfaceSugaroidQt(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.bot = BotRequests(self)

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

    def refresh(self):
        if str(self.chatbox.text()).isspace():
            return

        self.bot.start()
        """
        text = self.chatbox.text()
        self.conv.addItem("you: {}".format(text))
        QtCore.QCoreApplication.processEvents()

        response = self.parent.parse(text)
        self.conv.addItem("sugaroid: {}".format(str(response)))
        """

