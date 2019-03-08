# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PowerSynthAdd.ui'
#
# Created: Thu Feb 21 14:16:52 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(429, 139)
        self.editName = QtGui.QPlainTextEdit(Dialog)
        self.editName.setGeometry(QtCore.QRect(20, 50, 91, 31))
        self.editName.setObjectName("editName")
        self.editSchool = QtGui.QPlainTextEdit(Dialog)
        self.editSchool.setGeometry(QtCore.QRect(300, 50, 91, 31))
        self.editSchool.setObjectName("editSchool")
        self.addButton = QtGui.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(310, 90, 75, 23))
        self.addButton.setObjectName("addButton")
        self.editGPA = QtGui.QPlainTextEdit(Dialog)
        self.editGPA.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.editGPA.setObjectName("editGPA")
        self.labelGPA = QtGui.QLabel(Dialog)
        self.labelGPA.setGeometry(QtCore.QRect(150, 30, 46, 13))
        self.labelGPA.setObjectName("labelGPA")
        self.labelSchool = QtGui.QLabel(Dialog)
        self.labelSchool.setGeometry(QtCore.QRect(300, 30, 46, 13))
        self.labelSchool.setObjectName("labelSchool")
        self.labelName = QtGui.QLabel(Dialog)
        self.labelName.setGeometry(QtCore.QRect(20, 30, 46, 13))
        self.labelName.setObjectName("labelName")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.labelGPA.setText(QtGui.QApplication.translate("Dialog", "GPA:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSchool.setText(QtGui.QApplication.translate("Dialog", "School:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelName.setText(QtGui.QApplication.translate("Dialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))

