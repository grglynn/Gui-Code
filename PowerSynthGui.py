# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PowerSynthGui.ui'
#
# Created: Thu Feb 21 14:28:55 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_setDialog(object):
    def setupUi(self, setDialog):
        setDialog.setObjectName("setDialog")
        setDialog.resize(400, 125)
        self.nameLabel = QtGui.QLabel(setDialog)
        self.nameLabel.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.nameLabel.setObjectName("nameLabel")
        self.GPALabel = QtGui.QLabel(setDialog)
        self.GPALabel.setGeometry(QtCore.QRect(140, 10, 46, 13))
        self.GPALabel.setObjectName("GPALabel")
        self.schoolLabel = QtGui.QLabel(setDialog)
        self.schoolLabel.setGeometry(QtCore.QRect(290, 10, 46, 13))
        self.schoolLabel.setObjectName("schoolLabel")
        self.setButton = QtGui.QPushButton(setDialog)
        self.setButton.setGeometry(QtCore.QRect(310, 90, 75, 23))
        self.setButton.setObjectName("setButton")
        self.nameEdit = QtGui.QPlainTextEdit(setDialog)
        self.nameEdit.setGeometry(QtCore.QRect(10, 30, 91, 31))
        self.nameEdit.setObjectName("nameEdit")
        self.gpaEdit = QtGui.QPlainTextEdit(setDialog)
        self.gpaEdit.setGeometry(QtCore.QRect(140, 30, 111, 31))
        self.gpaEdit.setObjectName("gpaEdit")
        self.schoolEdit = QtGui.QPlainTextEdit(setDialog)
        self.schoolEdit.setGeometry(QtCore.QRect(290, 30, 91, 31))
        self.schoolEdit.setObjectName("schoolEdit")

        self.retranslateUi(setDialog)
        QtCore.QMetaObject.connectSlotsByName(setDialog)

    def retranslateUi(self, setDialog):
        setDialog.setWindowTitle(QtGui.QApplication.translate("setDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("setDialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.GPALabel.setText(QtGui.QApplication.translate("setDialog", "GPA:", None, QtGui.QApplication.UnicodeUTF8))
        self.schoolLabel.setText(QtGui.QApplication.translate("setDialog", "School:", None, QtGui.QApplication.UnicodeUTF8))
        self.setButton.setText(QtGui.QApplication.translate("setDialog", "Set", None, QtGui.QApplication.UnicodeUTF8))

