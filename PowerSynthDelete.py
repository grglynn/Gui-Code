# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PowerSynthDelete.ui'
#
# Created: Thu Feb 21 14:28:12 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_deleteDialog(object):
    def setupUi(self, deleteDialog):
        deleteDialog.setObjectName("deleteDialog")
        deleteDialog.resize(263, 106)
        self.nameLabel = QtGui.QPlainTextEdit(deleteDialog)
        self.nameLabel.setGeometry(QtCore.QRect(30, 50, 91, 31))
        self.nameLabel.setObjectName("nameLabel")
        self.deleteButton = QtGui.QPushButton(deleteDialog)
        self.deleteButton.setGeometry(QtCore.QRect(150, 60, 75, 23))
        self.deleteButton.setObjectName("deleteButton")
        self.labelName = QtGui.QLabel(deleteDialog)
        self.labelName.setGeometry(QtCore.QRect(30, 30, 46, 13))
        self.labelName.setObjectName("labelName")

        self.retranslateUi(deleteDialog)
        QtCore.QMetaObject.connectSlotsByName(deleteDialog)

    def retranslateUi(self, deleteDialog):
        deleteDialog.setWindowTitle(QtGui.QApplication.translate("deleteDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteButton.setText(QtGui.QApplication.translate("deleteDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("deleteDialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))

