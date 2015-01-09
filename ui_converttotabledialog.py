# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\documenti\dev\postgisQueryBuilder\ui-converttotabledialog.ui'
#
# Created: Fri Jan 09 10:07:18 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_convertToTableDialog(object):
    def setupUi(self, convertToTableDialog):
        convertToTableDialog.setObjectName(_fromUtf8("convertToTableDialog"))
        convertToTableDialog.resize(400, 98)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(convertToTableDialog)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(convertToTableDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tableNameString = QtGui.QLineEdit(convertToTableDialog)
        self.tableNameString.setObjectName(_fromUtf8("tableNameString"))
        self.verticalLayout.addWidget(self.tableNameString)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.deleteViewCheck = QtGui.QCheckBox(convertToTableDialog)
        self.deleteViewCheck.setObjectName(_fromUtf8("deleteViewCheck"))
        self.horizontalLayout.addWidget(self.deleteViewCheck)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(convertToTableDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(convertToTableDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), convertToTableDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), convertToTableDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(convertToTableDialog)

    def retranslateUi(self, convertToTableDialog):
        convertToTableDialog.setWindowTitle(QtGui.QApplication.translate("convertToTableDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("convertToTableDialog", "Table name", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteViewCheck.setText(QtGui.QApplication.translate("convertToTableDialog", "delete view", None, QtGui.QApplication.UnicodeUTF8))

