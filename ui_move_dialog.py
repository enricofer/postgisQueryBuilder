# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\dev\postgisQueryBuilder\ui_move_dialog.ui'
#
# Created: Fri Sep 11 13:16:41 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_moveDialog(object):
    def setupUi(self, moveDialog):
        moveDialog.setObjectName(_fromUtf8("moveDialog"))
        moveDialog.resize(340, 77)
        self.horizontalLayout = QtGui.QHBoxLayout(moveDialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.moveCombo = QtGui.QComboBox(moveDialog)
        self.moveCombo.setEditable(True)
        self.moveCombo.setObjectName(_fromUtf8("moveCombo"))
        self.verticalLayout.addWidget(self.moveCombo)
        self.buttonBox = QtGui.QDialogButtonBox(moveDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(moveDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), moveDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), moveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(moveDialog)

    def retranslateUi(self, moveDialog):
        moveDialog.setWindowTitle(_translate("moveDialog", "Dialog", None))

