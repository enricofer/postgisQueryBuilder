# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DEMO\Dropbox\dev\postgisQueryBuilder\ui_rename_dialog.ui'
#
# Created: Mon Sep 07 22:27:00 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_renameDialog(object):
    def setupUi(self, renameDialog):
        renameDialog.setObjectName(_fromUtf8("renameDialog"))
        renameDialog.resize(340, 75)
        self.horizontalLayout = QtGui.QHBoxLayout(renameDialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.renameString = QtGui.QLineEdit(renameDialog)
        self.renameString.setObjectName(_fromUtf8("renameString"))
        self.verticalLayout.addWidget(self.renameString)
        self.buttonBox = QtGui.QDialogButtonBox(renameDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(renameDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), renameDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), renameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(renameDialog)

    def retranslateUi(self, renameDialog):
        renameDialog.setWindowTitle(_translate("renameDialog", "Dialog", None))

