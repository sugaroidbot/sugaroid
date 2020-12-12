# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from . import rsrc_rc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 741)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/home/sugaroid.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "QPushButton {\n"
            "    border-radius: 25px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
            "    color: rgb(0, 0, 0);\n"
            "}\n"
            "QPushButton:pressed {\n"
            "    border-radius: 25px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 255, 255, 255), stop:1 rgba(0, 255, 152, 255));\n"
            "    color: rgb(0, 0, 0);\n"
            "}\n"
            ".QPushButton:hover {\n"
            "    border-radius: 25px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 199, 199, 255), stop:1 rgba(0, 190, 113, 255));\n"
            "    color: rgb(0, 0, 0);\n"
            " }\n"
            "QLineEdit {\n"
            "padding-left: 15px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(31, 31, 31, 255), stop:1 rgba(0, 0, 0, 255));\n"
            "        border-radius: 25px;\n"
            "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.push = QtWidgets.QPushButton(self.centralwidget)
        self.push.setMinimumSize(QtCore.QSize(50, 50))
        self.push.setMaximumSize(QtCore.QSize(50, 16777215))
        self.push.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ux/send.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.push.setIcon(icon1)
        self.push.setObjectName("push")
        self.gridLayout.addWidget(self.push, 3, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(256, 256))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/home/sugaroid.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.conv = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(15)
        self.conv.setFont(font)
        self.conv.setStyleSheet(
            "alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 68, 255, 255), stop:1 rgba(85, 0, 255, 255));")
        self.conv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.conv.setAlternatingRowColors(True)
        self.conv.setProperty("isWrapping", False)
        self.conv.setWordWrap(True)
        self.conv.setObjectName("conv")
        self.gridLayout.addWidget(self.conv, 2, 0, 1, 5)
        self.chatbox = QtWidgets.QLineEdit(self.centralwidget)
        self.chatbox.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(14)
        self.chatbox.setFont(font)
        self.chatbox.setClearButtonEnabled(True)
        self.chatbox.setObjectName("chatbox")
        self.gridLayout.addWidget(self.chatbox, 3, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sugaroid GUI"))
        self.centralwidget.setStatusTip(_translate(
            "MainWindow", "Created by Srevin Saju. Licensed under MIT 2020"))
        self.push.setStatusTip(_translate("MainWindow", "Send your message"))
        self.conv.setStatusTip(_translate(
            "MainWindow", "Sent messages come here"))
        self.chatbox.setStatusTip(_translate(
            "MainWindow", "Enter your message here"))
