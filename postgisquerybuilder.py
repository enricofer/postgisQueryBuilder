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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *
from PyQt4 import uic
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from postgisquerybuilderdialog import postgisQueryBuilderDialog
from querySetbuilder import querySet
from PSQL import PSQL

import os.path
import webbrowser


class postgisQueryBuilder:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'postgisquerybuilder_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        #self.dlg = postgisQueryBuilderDialog()
        self.dlg = uic.loadUi( os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), "ui_postgisquerybuilder.ui" ) )
        self.querySet = querySet()
        self.PSQL = PSQL(self.iface)
        


    def eventsConnect(self):
        self.dlg.QueryType.activated.connect(self.setQueryType)
        self.dlg.LAYERa.activated.connect(self.setLAYERa)
        self.dlg.LAYERb.activated.connect(self.setLAYERb)
        self.dlg.FIELD.activated.connect(self.setFIELD)
        self.dlg.OPERATOR.activated.connect(self.setOPERATOR)
        self.dlg.SPATIALREL.activated.connect(self.setSPATIALREL)
        self.dlg.SPATIALRELNOT.clicked.connect(self.setSPATIALRELNOT)
        self.dlg.checkCreateView.clicked.connect(self.checkCreateView)
        self.dlg.BUFFERRADIUS.textChanged.connect(self.setBUFFERRADIUS)
        self.dlg.CONDITION.activated.connect(self.setCONDITION)
        self.dlg.CONDITION.editTextChanged.connect(self.setCONDITION)
        self.dlg.ButtonRun.clicked.connect(self.runQuery)
        self.dlg.ButtonReset.clicked.connect(self.resetForm)
        self.dlg.ButtonClose.clicked.connect(self.closeDialog)
        self.dlg.ButtonHelp.clicked.connect(self.helpDialog)
        self.dlg.fieldsListA.clicked.connect(self.setFieldsList)
        self.dlg.checkMaterialized.clicked.connect(self.setMaterialized)

    def eventsDisconnect(self):
        self.dlg.QueryType.activated.disconnect(self.setQueryType)
        self.dlg.LAYERa.activated.disconnect(self.setLAYERa)
        self.dlg.LAYERb.activated.disconnect(self.setLAYERb)
        self.dlg.FIELD.activated.disconnect(self.setFIELD)
        self.dlg.OPERATOR.activated.disconnect(self.setOPERATOR)
        self.dlg.SPATIALREL.activated.disconnect(self.setSPATIALREL)
        self.dlg.SPATIALRELNOT.clicked.disconnect(self.setSPATIALRELNOT)
        self.dlg.checkCreateView.clicked.disconnect(self.checkCreateView)
        self.dlg.BUFFERRADIUS.textChanged.disconnect(self.setBUFFERRADIUS)
        self.dlg.CONDITION.activated.disconnect(self.setCONDITION)
        self.dlg.CONDITION.editTextChanged.disconnect(self.setCONDITION)
        self.dlg.ButtonRun.clicked.disconnect(self.runQuery)
        self.dlg.ButtonReset.clicked.disconnect(self.resetForm)
        self.dlg.ButtonClose.clicked.disconnect(self.closeDialog)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/postgisquerybuilder/querybuilderlogo.png"),
            u"postgisQueryBuilder", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToDatabaseMenu(u"&postgisQueryBuilder", self.action)
        self.populateGui()
        self.eventsConnect()

    def populateGui(self):
        self.dlg.GEOMETRYFIELD.setText("the_geom")
        self.dlg.KEYFIELD.setText("ogc_fid")
        self.populateComboBox(self.dlg.QueryType,self.querySet.getQueryLabels(),"Select query type",True)
        self.populateComboBox(self.dlg.OPERATOR,["=","<>",">","<","<=",">="],"Select",True)
        self.populateComboBox(self.dlg.SPATIALREL,self.querySet.getSpatialRelationships(),"Select spatial relationship",True)
        self.dlg.tabWidget.setCurrentIndex(0)
        #self.recurseChild(self.dlg,"")

    def recurseChild(self,slot,tab):
        # for testing: prints qt object tree
        for child in slot.children():
            print tab,"|",child.objectName()
            if child.children() != []:
                self.recurseChild(child,tab + "   ")

    def disableDialogSlot(self,slot):
        for child in self.dlg.tabWidget.widget(1).children():
            if child.objectName() == slot:
                child.setDisabled(True)

    def hideDialogSlot(self,slot):
        for child in self.dlg.tabWidget.widget(1).children():
            if child.objectName() == slot:
                child.hide()

    def showDialogSlot(self,slot):
        for child in self.dlg.tabWidget.widget(1).children():
            if child.objectName() == slot:
                child.show()

    def enableDialogSlot(self,slot):
        print slot
        for child in self.dlg.tabWidget.widget(1).children():
            if child.objectName() == slot:
                print "Enabled"
                child.setEnabled(True)

    def clearDialogSlot(self,slot):
        for child in self.dlg.tabWidget.widget(1).children():
            if child.objectName() == slot:
                child.clear()

    def checkCreateView(self):
        #method called when checkbox createview is clicked
        if self.dlg.checkCreateView.checkState():
            self.dlg.QueryName.setEnabled(True)
            self.dlg.checkMaterialized.setEnabled(True)
        else:
            self.dlg.QueryName.setDisabled(True)
            self.dlg.checkMaterialized.setDisabled(True)
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()

    def helpDialog(self):
        if self.dlg.QueryType.currentText() != "Select query type":
            webbrowser.open_new(self.querySet.getHelp())

    def setMaterialized(self):
        self.queryGen()

    def populateComboBox(self,combo,list,predef,sort):
        #procedure to fill specified combobox with provided list
        print combo.objectName()
        combo.clear()
        model=QStandardItemModel(combo)
        for elem in list:
            item = QStandardItem(str(elem))
            model.appendRow(item)
        if sort:
            model.sort(0)
        combo.setModel(model)
        if predef != "":
            combo.insertItem(0,predef)
            combo.setCurrentIndex(0)



    def setLAYERa(self):
        #called when LAYERa is activated
        if self.dlg.LAYERa.currentText()[:6] == "Select":
            return
        self.querySet.setParameter("LAYERa",self.dlg.LAYERa.currentText())
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()
        self.populateComboBox(self.dlg.FIELD,self.PSQL.getFieldsContent(self.dlg.LAYERa.currentText()),"Select field",True)
        if not self.PSQL.testIfFidExist(self.PSQL.getFieldsContent(self.dlg.LAYERa.currentText())):
            self.querySet.setFIDFIELD()
        self.addListToFieldTable("A",self.PSQL.getFieldsContent(self.dlg.LAYERa.currentText()))
        

    def setLAYERb(self):
        #called when LAYERb is activated
        if self.dlg.LAYERb.currentText()[:6] == "Select":
            return
        self.querySet.setParameter("LAYERb",self.dlg.LAYERb.currentText())
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()
        self.addListToFieldTable("B",self.PSQL.getFieldsContent(self.dlg.LAYERb.currentText()))

    def addListToFieldTable(self,suff,fl):
        #called to populate field list for WHERE statement
        if suff == 'A':
            wdgt=self.dlg.fieldsListA
        else:
            wdgt=self.dlg.fieldsListB
        wdgt.clear()
        for row in fl:
            item=QListWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            item.setText(row)
            #exclude geometryfield from user options when postgis query
            if self.geoQuery and row == self.querySet.getParameter("GEOMETRYFIELD"):
                item.setFlags(item.flags() ^ Qt.ItemIsEnabled)
            else:
                item.setFlags(item.flags() | Qt.ItemIsEnabled)
            wdgt.addItem(item)

    def setFieldsList(self):
        # procedure to resume selected fields to SELECT statements
        items = []
        for index in xrange(self.dlg.fieldsListA.count()):
             if self.dlg.fieldsListA.item(index).checkState() == Qt.Checked:
                items.append('"'+self.dlg.LAYERa.currentText()+'".'+self.dlg.fieldsListA.item(index).text())
        for index in xrange(self.dlg.fieldsListB.count()):
             if self.dlg.fieldsListB.item(index).checkState() == Qt.Checked:
                items.append('"%s"'%(self.dlg.LAYERb.currentText())+self.dlg.fieldsListB.item(index).text())
        #print items
        self.querySet.setFieldsSet(items)
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()

    def setFIELD(self):
        if self.dlg.FIELD.currentText()[:6] == "Select":
            return
        self.querySet.setParameter("FIELD",self.dlg.FIELD.currentText())
        fType = self.PSQL.getFieldsType(self.querySet.getParameter("LAYERa"),self.dlg.FIELD.currentText())
        fType = fType[:4]
        #print fType
        if ((fType == "char") or (fType == "text")):
            self.tDelimiter = "'"
        else:
            self.tDelimiter = ""
        self.populateComboBox(self.dlg.OPERATOR,["=","<>",">","<","<=",">="],"Select",True)
        self.populateComboBox(self.dlg.CONDITION,self.PSQL.getUniqeValues(self.querySet.getParameter("LAYERa"),self.dlg.FIELD.currentText(),100),"",True)
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()


    def setOPERATOR(self):
        if self.dlg.OPERATOR.currentText()[:6] == "Select":
            return
        self.querySet.setParameter("OPERATOR",self.dlg.OPERATOR.currentText())
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()

    def setSPATIALREL(self):
        if self.dlg.SPATIALREL.currentText()[:6] == "Select":
            return
        self.querySet.setParameter("SPATIALREL",self.dlg.SPATIALREL.currentText())
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()
            
    def setBUFFERRADIUS(self):
        self.querySet.setParameter("BUFFERRADIUS",self.dlg.BUFFERRADIUS.text())
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()
            
    def setCONDITION(self):
        self.querySet.setParameter("CONDITION",self.tDelimiter+self.dlg.CONDITION.currentText()+self.tDelimiter)
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()

    def setCONDITIONtext(self):
        self.querySet.setParameter("CONDITION",self.dlg.CONDITION.currentText())
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()

    def setSPATIALRELNOT(self):
        if self.dlg.SPATIALRELNOT.isChecked():
            self.querySet.setParameter("SPATIALRELNOT","NOT ")
        else:
            self.querySet.setParameter("SPATIALRELNOT"," ")
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()

    def setQueryName(self):
        self.querySet.setParameter("VIEWNAME",self.dlg.QueryName.text())
        if self.querySet.testQueryParametersCheckList():
            self.dlg.QueryResult.setPlainText(self.querySet.getQueryParsed(self.dlg.checkCreateView.checkState()))

    def queryGen(self):
        self.querySet.setParameter("GEOMETRYFIELD",self.dlg.GEOMETRYFIELD.text())
        self.querySet.setParameter("KEYFIELD",self.dlg.KEYFIELD.text())
        if self.dlg.checkCreateView.checkState():
            self.enableDialogSlot("QueryName")
        if self.dlg.checkMaterialized.checkState():
            self.querySet.setParameter("MATERIALIZED","MATERIALIZED")
        else:
            self.querySet.setParameter("MATERIALIZED","")
        self.enableDialogSlot("QueryResult")
        self.enableDialogSlot("checkCreateView")
        self.enableDialogSlot("AddToMap")
        qName = self.querySet.getNameParsed()
        self.dlg.QueryName.setText(qName)
        self.querySet.setParameter("VIEWNAME",qName)
        self.dlg.QueryResult.setPlainText(self.querySet.getQueryParsed(self.dlg.checkCreateView.checkState()))
        self.dlg.QueryName.textChanged.connect(self.setQueryName)

    def setQueryType(self,line):
        theQ = self.dlg.QueryType.currentText()
        if theQ[:6] == "Select":
            return
        #self.querySet.resetParameters()
        self.resetDialog()
        self.querySet.setCurrentQuery(theQ)
        if theQ[:2]=="ST":
            self.geoQuery = True
        else:
            self.geoQuery = None
        for slot in self.querySet.getRequiredSlots():
            #print slot
            self.enableDialogSlot(slot)
            self.showDialogSlot(slot)
            self.showDialogSlot(slot+"Label")
        print self.querySet.testQueryParametersCheckList()
        self.dlg.Helper.setText(self.querySet.getDescription())
        

    def resetDialog(self):
        self.eventsDisconnect()
        self.clearAllDialogs()
        self.querySet.resetParameters()
        self.disableQueryDefSlot()
        self.hideQueryDefSlot()
        tables = self.PSQL.getLayers()
        self.populateComboBox(self.dlg.LAYERa,tables,"Select Layer",True)
        self.populateComboBox(self.dlg.LAYERb,tables,"Select Layer",True)
        self.eventsConnect()

    def hideQueryDefSlot(self):
        toHide=["BUFFERRADIUS","FIELD","OPERATOR","CONDITION","SPATIALREL","SPATIALRELNOT","LAYERaLabel","BUFFERRADIUSLabel","FIELDLabel","OPERATORLabel","CONDITIONLabel","SPATIALRELLabel","SPATIALRELNOTLabel","fieldsListALabel","fieldsListBLabel"]
        for slot in toHide:
            self.hideDialogSlot(slot)

    def clearQueryDefSlot(self):
        toClear=["LAYERa","LAYERb","BUFFERRADIUS","FIELD","OPERATOR","CONDITION","SPATIALREL","fieldsListA","fieldsListB","LAYERaLabel","LAYERbLabel","BUFFERRADIUSLabel","FIELDLabel","OPERATORLabel","CONDITIONLabel","SPATIALRELLabel","fieldsListALabel","fieldsListBLabel"]
        for slot in toClear:
            self.clearDialogSlot(slot)

    def disableQueryDefSlot(self):
        toDisable=["LAYERa","LAYERb","BUFFERRADIUS","FIELD","OPERATOR","CONDITION","SPATIALREL","SPATIALRELNOT","fieldsListA","fieldsListB"]
        for slot in toDisable:
            self.disableDialogSlot(slot)

    def clearAllDialogs(self):
        self.dlg.LAYERa.clear()
        self.dlg.LAYERb.clear()
        self.dlg.BUFFERRADIUS.clear()
        self.dlg.FIELD.clear()
        self.dlg.CONDITION.clear()
        #self.dlg.SPATIALRELNOT.setDisabled(True)
        #self.dlg.QueryType.clear()
        self.dlg.QueryResult.clear()
        self.dlg.QueryName.clear()
        #self.dlg.OPERATOR.clear()
        #self.dlg.SPATIALREL.clear()
        self.dlg.fieldsListA.clear()
        self.dlg.fieldsListB.clear()
        self.dlg.TableResult.clear()
        self.dlg.SPATIALRELNOT.setCheckState(Qt.Unchecked)

    def getPSQLConnections(self):
        conn = self.PSQL.getConnections()
        self.populateComboBox(self.dlg.PSQLConnection,conn,"Select connection",True)
        self.dlg.PSQLConnection.activated.connect(self.setConnection)

    def closeDialog(self):
        self.resetDialog()
        self.dlg.hide()

    def resetForm(self):
        self.resetDialog()
        self.populateGui()
        self.dlg.tabWidget.setCurrentIndex(1)
        

    def setConnection(self):
        self.PSQL.setConnection(self.dlg.PSQLConnection.currentText())
        print "SCHEMAS",self.PSQL.getSchemas()
        self.populateComboBox(self.dlg.DBSchema,self.PSQL.getSchemas(),"Select schema",True)
        self.dlg.DBSchema.activated.connect(self.loadPSQLLayers)


    def loadPSQLLayers(self):
        if self.dlg.DBSchema.currentText() != "Select schema":
            self.PSQL.setSchema(self.dlg.DBSchema.currentText())
            self.populateGui()
            self.resetDialog()
            self.dlg.tabWidget.setCurrentIndex(1)

    def runQuery(self):
        #method to run generated query
        self.PSQL.tableResultGen(self.dlg.QueryResult.toPlainText(),self.dlg.TableResult)
        self.dlg.tabWidget.setCurrentIndex(3)

        if self.dlg.AddToMap.checkState():
            if self.dlg.checkCreateView.checkState():
                self.PSQL.loadView(self.querySet.getParameter("VIEWNAME"),self.querySet.getParameter("GEOMETRYFIELD"))
            else:
                self.PSQL.loadSql(self.querySet.getParameter("VIEWNAME"),self.dlg.QueryResult.toPlainText(),self.querySet.getParameter("GEOMETRYFIELD"))

    def tableResultGen(self):
        self.PSQL.test()

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&postgisQueryBuilder", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        self.getPSQLConnections()
        
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass
