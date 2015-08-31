# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\DEMO\Dropbox\dev\postgisQueryBuilder\ui_askcredentialdialog.ui'
#
# Created: Mon Aug 31 16:48:54 2015
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

class Ui_askcredentialdialog(object):
    def setupUi(self, askcredentialdialog):
        askcredentialdialog.setObjectName(_fromUtf8("askcredentialdialog"))
        askcredentialdialog.resize(178, 156)
        self.verticalLayout = QtGui.QVBoxLayout(askcredentialdialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(askcredentialdialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.user_edit = QtGui.QLineEdit(askcredentialdialog)
        self.user_edit.setObjectName(_fromUtf8("user_edit"))
        self.verticalLayout.addWidget(self.user_edit)
        self.label_2 = QtGui.QLabel(askcredentialdialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.password_edit = QtGui.QLineEdit(askcredentialdialog)
        self.password_edit.setEchoMode(QtGui.QLineEdit.Password)
        self.password_edit.setObjectName(_fromUtf8("password_edit"))
        self.verticalLayout.addWidget(self.password_edit)
        self.messageBox = QtGui.QLabel(askcredentialdialog)
        self.messageBox.setText(_fromUtf8(""))
        self.messageBox.setWordWrap(True)
        self.messageBox.setObjectName(_fromUtf8("messageBox"))
        self.verticalLayout.addWidget(self.messageBox)
        self.buttonBox = QtGui.QDialogButtonBox(askcredentialdialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(askcredentialdialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), askcredentialdialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), askcredentialdialog.reject)
        QtCore.QMetaObject.connectSlotsByName(askcredentialdialog)

    def retranslateUi(self, askcredentialdialog):
        askcredentialdialog.setWindowTitle(_translate("askcredentialdialog", "Dialog", None))
        self.label.setText(_translate("askcredentialdialog", "User:", None))
        self.label_2.setText(_translate("askcredentialdialog", "Password:", None))

