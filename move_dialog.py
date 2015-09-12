# -*- coding: utf-8 -*-
"""
/***************************************************************************
 move_dialog
                                 A QGIS plugin
 helps to build query in postgis
                             -------------------
        begin                : 2014-04-24
        copyright            : (C) 2014 by Enrico Ferreguti
        email                : enricofer@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_move_dialog import Ui_moveDialog


class moveDialog(QtGui.QDialog, Ui_moveDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.hide()
        self.buttonBox.accepted.connect(self.acceptRename)
        self.buttonBox.rejected.connect(self.rejectRename)
        self.acceptedFlag = None
        self.createFlag = None

    def acceptRename(self):
        self.acceptedFlag = True

    def rejectRename(self):
        self.acceptedFlag = None

    @staticmethod
    def getNewSchema(parent):
        schemas = parent.PSQL.getSchemas()
        dialog = moveDialog()
        dialog.moveCombo.addItems(schemas)
        result = dialog.exec_()
        #dialog.show()
        if not dialog.moveCombo.currentText() in schemas:
            parent.PSQL.addSchema(dialog.moveCombo.currentText())
            parent.dlg.DBSchema.addItem(dialog.moveCombo.currentText())
        if dialog.acceptedFlag:
            return (dialog.moveCombo.currentText())
        else:
            return None
            
