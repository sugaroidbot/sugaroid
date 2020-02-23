# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sugaroid/gui/ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 521, 451))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.push = QtWidgets.QPushButton(self.widget)
        self.push.setObjectName("push")
        self.gridLayout.addWidget(self.push, 1, 1, 1, 1)
        self.chatbox = QtWidgets.QLineEdit(self.widget)
        self.chatbox.setObjectName("chatbox")
        self.gridLayout.addWidget(self.chatbox, 1, 0, 1, 1)
        self.conv = QtWidgets.QListWidget(self.widget)
        font = QtGui.QFont()
        font.setFamily("Titillium Web")
        font.setPointSize(15)
        self.conv.setFont(font)
        self.conv.setStyleSheet("alternate-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 68, 255, 255), stop:1 rgba(85, 0, 255, 255));")
        self.conv.setAlternatingRowColors(True)
        self.conv.setProperty("isWrapping", False)
        self.conv.setWordWrap(True)
        self.conv.setObjectName("conv")
        self.gridLayout.addWidget(self.conv, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 30))
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
        self.push.setText(_translate("MainWindow", "OK"))
