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
from PyQt4 import QtGui

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
        self.dlg = postgisQueryBuilderDialog()
        #self.dlg = uic.loadUi( os.path.join( os.path.dirname( os.path.abspath( __file__ ) ), "ui_postgisquerybuilder.ui" ) )
        self.querySet = querySet()
        self.PSQL = PSQL(self.iface)
        


    def eventsConnect(self):
        self.dlg.QueryType.activated.connect(self.setQueryType)
        self.dlg.LAYERa.activated.connect(self.setLAYERa)
        self.dlg.LAYERb.activated.connect(self.setLAYERb)
        self.dlg.FIELD.activated.connect(self.setFIELD)
        self.dlg.OPERATOR.activated.connect(self.setOPERATOR)
        self.dlg.DISTANCEOP.activated.connect(self.setDISTANCEOP)
        self.dlg.SPATIALREL.activated.connect(self.setSPATIALREL)
        self.dlg.SPATIALRELNOT.stateChanged.connect(self.setSPATIALRELNOT)
        self.dlg.checkCreateView.clicked.connect(self.checkCreateView)
        self.dlg.BUFFERRADIUS.textChanged.connect(self.setBUFFERRADIUS)
        self.dlg.CONDITION.activated.connect(self.setCONDITION)
        self.dlg.CONDITION.editTextChanged.connect(self.setCONDITION)
        self.dlg.DISTANCE.textChanged.connect(self.setDISTANCE)
        self.dlg.ButtonRun.clicked.connect(self.runQuery)
        self.dlg.ButtonReset.clicked.connect(self.resetForm)
        self.dlg.ButtonClose.clicked.connect(self.closeDialog)
        self.dlg.ButtonHelp.clicked.connect(self.helpDialog)
        self.dlg.fieldsListA.clicked.connect(self.setFieldsList)
        self.dlg.fieldsListB.clicked.connect(self.setFieldsList)
        self.dlg.checkMaterialized.clicked.connect(self.setMaterialized)
        self.dlg.AddToMapButton.clicked.connect(self.layerAddToMap)
        self.dlg.GetInfoButton.clicked.connect(self.layerGetTable)
        self.dlg.DeleteButton.clicked.connect(self.layerDelete)
        self.dlg.RefreshButton.clicked.connect(self.layerRefresh)
        self.dlg.JOIN.activated.connect(self.setJOIN)
        self.dlg.FIELDb.activated.connect(self.setFIELDb)

    def eventsDisconnect(self):
        self.dlg.QueryType.activated.disconnect(self.setQueryType)
        self.dlg.LAYERa.activated.disconnect(self.setLAYERa)
        self.dlg.LAYERb.activated.disconnect(self.setLAYERb)
        self.dlg.FIELD.activated.disconnect(self.setFIELD)
        self.dlg.OPERATOR.activated.disconnect(self.setOPERATOR)
        self.dlg.DISTANCEOP.activated.disconnect(self.setDISTANCEOP)
        self.dlg.SPATIALREL.activated.disconnect(self.setSPATIALREL)
        self.dlg.SPATIALRELNOT.stateChanged.disconnect(self.setSPATIALRELNOT)
        self.dlg.checkCreateView.clicked.disconnect(self.checkCreateView)
        self.dlg.BUFFERRADIUS.textChanged.disconnect(self.setBUFFERRADIUS)
        self.dlg.CONDITION.activated.disconnect(self.setCONDITION)
        self.dlg.CONDITION.editTextChanged.disconnect(self.setCONDITION)
        self.dlg.DISTANCE.textChanged.disconnect(self.setDISTANCE)
        self.dlg.ButtonRun.clicked.disconnect(self.runQuery)
        self.dlg.ButtonReset.clicked.disconnect(self.resetForm)
        self.dlg.ButtonClose.clicked.disconnect(self.closeDialog)
        self.dlg.AddToMapButton.clicked.disconnect(self.layerAddToMap)
        self.dlg.GetInfoButton.clicked.disconnect(self.layerGetTable)
        self.dlg.DeleteButton.clicked.disconnect(self.layerDelete)
        self.dlg.RefreshButton.clicked.disconnect(self.layerRefresh)
        self.dlg.JOIN.activated.disconnect(self.setJOIN)
        self.dlg.FIELDb.activated.disconnect(self.setFIELDb)
        self.dlg.fieldsListA.clicked.disconnect(self.setFieldsList)
        self.dlg.fieldsListB.clicked.disconnect(self.setFieldsList)

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
        self.populateComboBox(self.dlg.DISTANCEOP,["=","<>",">","<","<=",">="],"Select",True)
        self.populateComboBox(self.dlg.JOIN,["INNER JOIN","CROSS JOIN","RIGHT OUTER JOIN","LEFT OUTER JOIN","FULL OUTER JOIN"],"Select",True)
        self.populateComboBox(self.dlg.SPATIALREL,self.querySet.getSpatialRelationships(),"Select spatial relationship",True)
        self.dlg.tabWidget.setCurrentIndex(0)
        #self.recurseChild(self.dlg,"")

    def layerAddToMap(self):
        for rowList in range(0,self.dlg.LayerList.count()):
            rowCheckbox = self.dlg.LayerList.item(rowList)
            #take only selected attributes by checkbox
            if rowCheckbox.checkState() == Qt.Checked:
                self.PSQL.loadView(rowCheckbox.text(),self.dlg.GEOMETRYFIELD.text(),self.dlg.KEYFIELD.text())
        self.uncheckList(self.dlg.LayerList)

    def layerGetTable(self):
        for rowList in range(0,self.dlg.LayerList.count()):
            rowCheckbox = self.dlg.LayerList.item(rowList)
            #take only selected attributes by checkbox
            if rowCheckbox.checkState() == Qt.Checked:
                self.PSQL.tableResultGen(rowCheckbox.text(),"",self.dlg.TableResult)
                self.dlg.tabWidget.setCurrentIndex(3)
                self.uncheckList(self.dlg.LayerList)
                break

    def layerDelete(self):
        for rowList in range(0,self.dlg.LayerList.count()):
            rowCheckbox = self.dlg.LayerList.item(rowList)
            #take only selected attributes by checkbox
            if rowCheckbox.checkState() == Qt.Checked:
                msg = "Are you sure you want to delete layer '%s' ?" % rowCheckbox.text()
                reply = QMessageBox.question(None, 'Message', msg, QMessageBox.Yes, QMessageBox.No)
                if reply == QMessageBox.Yes:
                    result = self.PSQL.deleteLayer(rowCheckbox.text())
                    if result != "":
                        QMessageBox.information(None, "ERROR:", result)
                    else:
                        print "DELETED", rowCheckbox.text()
        self.populateLayerMenu()

    def layerRefresh(self):
        for rowList in range(0,self.dlg.LayerList.count()):
            rowCheckbox = self.dlg.LayerList.item(rowList)
            #take only selected attributes by checkbox
            if rowCheckbox.checkState() == Qt.Checked:
                if self.PSQL.isMaterializedView(rowCheckbox.text()): 
                    print self.PSQL.refreshMaterializedView(rowCheckbox.text())
        self.uncheckList(self.dlg.LayerList)

    def recurseChild(self,slot,tab):
        # for testing: prints qt object tree
        for child in slot.children():
            print tab,"|",child.objectName()
            if child.children() != []:
                self.recurseChild(child,tab + "   ")

    def uncheckList(self,slot):
        for row in range(0,slot.count()):
            self.dlg.LayerList.item(row).setCheckState(Qt.Unchecked);

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
        for child in self.dlg.tabWidget.widget(1).children():
            if child.objectName() == slot:
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
        combo.clear()
        model=QStandardItemModel(combo)
        for elem in list:
            try:
                item = QStandardItem(unicode(elem))
            except TypeError:
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
        self.addListToFieldTable(self.dlg.fieldsListA,self.PSQL.getFieldsContent(self.dlg.LAYERa.currentText()))
        

    def setLAYERb(self):
        #called when LAYERb is activated
        if self.dlg.LAYERb.currentText()[:6] == "Select":
            return
        self.querySet.setParameter("LAYERb",self.dlg.LAYERb.currentText())
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()
        self.addListToFieldTable(self.dlg.fieldsListB,self.PSQL.getFieldsContent(self.dlg.LAYERb.currentText()))
        self.populateComboBox(self.dlg.FIELDb,self.PSQL.getFieldsContent(self.dlg.LAYERb.currentText()),"Select field",True)

    def addListToFieldTable(self,fieldSlot,fl):
        #called to populate field list for WHERE statement
        wdgt=fieldSlot
        wdgt.clear()
        for row in fl:
            item=QListWidgetItem()
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            item.setText(row)
            #print row
            if self.PSQL.isTable(row):
                item.setIcon(QIcon(":/plugins/postgisquerybuilder/iT.png"))
            elif self.PSQL.isView(row):
                item.setIcon(QIcon(":/plugins/postgisquerybuilder/iV.png"))
            elif self.PSQL.isMaterializedView(row):
                item.setIcon(QIcon(":/plugins/postgisquerybuilder/iM.png"))
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
                items.append('"'+self.dlg.LAYERa.currentText()+'"."'+self.dlg.fieldsListA.item(index).text()+'"')
        for index in xrange(self.dlg.fieldsListB.count()):
             if self.dlg.fieldsListB.item(index).checkState() == Qt.Checked:
                items.append('"'+self.dlg.LAYERb.currentText()+'"."'+self.dlg.fieldsListB.item(index).text()+'"')
        #print "SELECTED FIELDS",items
        self.querySet.setFieldsSet(items)
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()

    def setFIELD(self):
        if self.dlg.FIELD.currentText()[:6] == "Select":
            return
        self.querySet.setParameter("FIELD",'"'+self.dlg.LAYERa.currentText()+'"."'+self.dlg.FIELD.currentText()+'"')
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

    def setFIELDb(self):
        if self.dlg.FIELDb.currentText()[:6] == "Select":
            return
        self.querySet.setParameter("FIELDb",'"'+self.dlg.LAYERb.currentText()+'"."'+self.dlg.FIELDb.currentText()+'"')
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()

    def setDISTANCEOP(self):
        if self.dlg.DISTANCEOP.currentText()[:6] == "Select":
            return
        self.querySet.setParameter("DISTANCEOP",self.dlg.DISTANCEOP.currentText())
        if self.querySet.testQueryParametersCheckList():
            self.queryGen()

    def setDISTANCE(self):
        self.querySet.setParameter("DISTANCE",self.dlg.DISTANCE.text())
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

    def setJOIN(self):
        self.querySet.setParameter("JOIN",self.dlg.JOIN.currentText())
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
        #print self.querySet.testQueryParametersCheckList()
        #simulate click on checkbox to set required slot
        self.dlg.SPATIALRELNOT.setCheckState(Qt.Checked)
        self.dlg.SPATIALRELNOT.setCheckState(Qt.Unchecked)
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
        self.geoQuery = None
        self.eventsConnect()

    def hideQueryDefSlot(self):
        toHide=["BUFFERRADIUS","FIELD","OPERATOR","CONDITION",\
                "SPATIALREL","SPATIALRELNOT","LAYERaLabel","BUFFERRADIUSLabel",\
                "FIELDLabel","OPERATORLabel","CONDITIONLabel","SPATIALRELLabel",
                "SPATIALRELNOTLabel","fieldsListALabel","fieldsListBLabel",\
                "DISTANCEOP","DISTANCE","DISTANCEOPLabel","DISTANCELabel","FIELDb","FIELDbLabel","JOIN","JOINLabel"]
        for slot in toHide:
            self.hideDialogSlot(slot)

    def clearQueryDefSlot(self):
        toClear=["LAYERa","LAYERb","BUFFERRADIUS","FIELD","FIELDb",\
                  "OPERATOR","CONDITION","SPATIALREL","fieldsListA","fieldsListB",\
                  "DISTANCEOP","DISTANCE","JOIN"]
        for slot in toClear:
            self.clearDialogSlot(slot)

    def disableQueryDefSlot(self):
        toDisable=["LAYERa","LAYERb","BUFFERRADIUS","FIELD","FIELDb",\
                    "OPERATOR","CONDITION","SPATIALREL",\
                    "SPATIALRELNOT","fieldsListA","fieldsListB",
                    "DISTANCEOP","DISTANCE","JOIN"]
        for slot in toDisable:
            self.disableDialogSlot(slot)

    def clearAllDialogs(self):
        self.dlg.LAYERa.clear()
        self.dlg.LAYERb.clear()
        self.dlg.BUFFERRADIUS.clear()
        self.dlg.FIELD.clear()
        self.dlg.CONDITION.clear()
        self.dlg.QueryResult.clear()
        self.dlg.QueryName.clear()
        self.dlg.fieldsListA.clear()
        self.dlg.fieldsListB.clear()
        self.dlg.TableResult.clear()
        self.dlg.SPATIALRELNOT.setCheckState(Qt.Unchecked)
        self.dlg.DISTANCE.clear()

    def getPSQLConnections(self):
        conn = self.PSQL.getConnections()
        self.populateComboBox(self.dlg.PSQLConnection,conn,"Select connection",True)
        self.hideQueryDefSlot()
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
        #print "SCHEMAS",self.PSQL.getSchemas()
        self.populateComboBox(self.dlg.DBSchema,self.PSQL.getSchemas(),"Select schema",True)
        self.dlg.DBSchema.activated.connect(self.loadPSQLLayers)


    def loadPSQLLayers(self):
        if self.dlg.DBSchema.currentText() != "Select schema":
            self.PSQL.setSchema(self.dlg.DBSchema.currentText())
            self.populateGui()
            self.resetDialog()
            #self.dlg.tabWidget.setCurrentIndex(1)
            self.querySet.setSchema(self.dlg.DBSchema.currentText())
            self.populateLayerMenu()

    def populateLayerMenu(self):
        self.addListToFieldTable(self.dlg.LayerList,self.PSQL.getLayers())

    def runQuery(self):
        #method to run generated query
        self.PSQL.tableResultGen(self.dlg.LAYERa.currentText(),self.dlg.QueryResult.toPlainText(),self.dlg.TableResult)
        self.dlg.tabWidget.setCurrentIndex(3)

        if self.dlg.AddToMap.checkState():
            if self.dlg.checkCreateView.checkState():
                self.PSQL.loadView(self.querySet.getParameter("VIEWNAME"),self.querySet.getParameter("GEOMETRYFIELD"),self.querySet.getParameter("KEYFIELD"))
            else:
                self.PSQL.loadSql(self.querySet.getParameter("VIEWNAME"),self.dlg.QueryResult.toPlainText(),self.querySet.getParameter("GEOMETRYFIELD"),self.querySet.getParameter("KEYFIELD"))

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
