# -*- coding: utf-8 -*-
"""
/***************************************************************************
 postgisQueryBuilder
                                 A QGIS plugin
 helps to build views in postgis
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

#from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_converttotabledialog import Ui_convertToTableDialog

import os
# create the dialog for zoom to point


class convertToTableDialog(QDialog, Ui_convertToTableDialog):
    def __init__(self,parent):
        QDialog.__init__(self)
        self.parent = parent
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.convert)
        self.buttonBox.rejected.connect(self.cancel)

    def ask(self,viewName):
        #QMessageBox.critical(None, "", "arrivato!")
        self.show()
        self.raise_()
        self.viewName = viewName
        self.tableNameString.setText(viewName+"_totable")
        self.tableNameString.setFocus()
        self.tableNameString.selectAll()

    def cancel(self):
        #self.hide()
        pass

    def convert(self):
        tableName = self.tableNameString.text()
        schema = self.parent.PSQL.schema
        q = 'CREATE TABLE "%s"."%s" as (SELECT * FROM "%s"."%s");' % (schema,tableName,schema,self.viewName)
        print q
        res = self.parent.PSQL.submitCommand(q)
        if not (res == "" or res == None or res == " "):
            QMessageBox.information(None, "ERROR:", res)
        else:
            if self.deleteViewCheck.isChecked():
                self.parent.PSQL.deleteLayer(self.viewName)
            self.parent.populateLayerMenu()
