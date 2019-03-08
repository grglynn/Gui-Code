# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PowerSynthFind.ui'
#
# Created: Thu Feb 21 14:28:25 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_findDialog(object):
    def setupUi(self, findDialog):
        findDialog.setObjectName("findDialog")
        findDialog.resize(271, 79)
        self.nameLabel = QtGui.QPlainTextEdit(findDialog)
        self.nameLabel.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.nameLabel.setObjectName("nameLabel")
        self.labelName = QtGui.QLabel(findDialog)
        self.labelName.setGeometry(QtCore.QRect(30, 10, 46, 13))
        self.labelName.setObjectName("labelName")
        self.findButton = QtGui.QPushButton(findDialog)
        self.findButton.setGeometry(QtCore.QRect(140, 30, 75, 23))
        self.findButton.setObjectName("findButton")

        self.retranslateUi(findDialog)
        QtCore.QMetaObject.connectSlotsByName(findDialog)

    def retranslateUi(self, findDialog):
        findDialog.setWindowTitle(QtGui.QApplication.translate("findDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("findDialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(QtGui.QApplication.translate("findDialog", "Find", None, QtGui.QApplication.UnicodeUTF8))

