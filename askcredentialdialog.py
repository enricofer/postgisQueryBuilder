# -*- coding: utf-8 -*-
"""
/***************************************************************************
 askcredentialDialog
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

from qgis.PyQt import QtCore, QtGui, QtWidgets, uic

import os

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'ui_askcredentialdialog.ui'))

# create the dialog for db credential


class askCredentialDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.messageBox.hide()
        self.hide()
        self.buttonBox.accepted.connect(self.acceptCredentials)
        self.buttonBox.rejected.connect(self.rejectCredentials)
        self.acceptedFlag = None

    def acceptCredentials(self):
        self.acceptedFlag = True

    def rejectCredentials(self):
        self.acceptedFlag = None

    def setUser(self,u):
        self.user_edit.setText(u)
        
    def setPassword(self,p):
        self.password_edit.setText(p)
        
    def getUser(self):
        return self.user_edit.text()
        
    def getPassword(self):
        return self.password_edit.text()

    def setMessage(self,message):
        self.messageBox.show()
        self.messageBox.setText(message)
        
    @staticmethod
    def form(defaultUser,defaultPassword,msg = None):
        dialog = askCredentialDialog()
        dialog.setUser(defaultUser)
        dialog.setPassword(defaultPassword)
        if msg or msg != "":
            dialog.setMessage(msg)
        result = dialog.exec_()
        dialog.show()
        return (dialog.acceptedFlag,dialog.getUser(),dialog.getPassword())
            
