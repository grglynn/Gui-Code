# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PowerSynthMain.ui'
#
# Created: Thu Feb 21 14:28:33 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(356, 106)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.FindAndEdt = QtGui.QPushButton(self.centralwidget)
        self.FindAndEdt.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.FindAndEdt.setObjectName("FindAndEdt")
        self.AddData = QtGui.QPushButton(self.centralwidget)
        self.AddData.setGeometry(QtCore.QRect(130, 40, 75, 23))
        self.AddData.setObjectName("AddData")
        self.DeleteData = QtGui.QPushButton(self.centralwidget)
        self.DeleteData.setGeometry(QtCore.QRect(250, 40, 75, 23))
        self.DeleteData.setObjectName("DeleteData")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.FindAndEdt.setText(QtGui.QApplication.translate("MainWindow", "Find and Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.AddData.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.DeleteData.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))

