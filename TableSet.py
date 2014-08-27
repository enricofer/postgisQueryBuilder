# -*- coding: utf-8 -*-
"""
/***************************************************************************
 postgisQueryBuilder/filterSet
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

from PyQt4 import QtGui, QtCore

class tableSet(QtGui.QTableWidget):

    def __init__(self,parent = None):
        #QtGui.QTableWidget.__init__(param)
        super (tableSet,self).__init__(parent)
        self.signalMapper = QtCore.QSignalMapper()
        self.signalMapper.mapped[QtGui.QWidget].connect(self.on_signalMapper_mapped)
        #self.twg = twg
        #self.layerList = layerList

    def populateFilterTable(self,PSQL,layerQuery):
        self.PSQL = PSQL
        self.layerList = self.PSQL.getLayers()
        self.layerQuery = layerQuery
        self.layerQueryFields = self.PSQL.getFieldsContent(layerQuery)
        self.clearContents()
        #self.layerList = layerList
        self.setRowCount(1)
        self.setColumnCount(4)
        self.setColumnWidth(0,90)
        self.setColumnWidth(1,210) 
        self.setColumnWidth(2,90) 
        self.setColumnWidth(3,210) 
        self.setCellWidget(0,0,self.actionFilterCell(0,0))
        

    def expopulateFilterTable(self,layerList):
        self.clearContents()
        self.layerList = layerList
        self.setRowCount(20)
        self.setColumnCount(5)
        #self.connect()
        self.cellActivated.connect(self.testSignal)
        for row in range (0,20):
            self.setCellWidget(row,0,self.junctionRow())
            
            self.setCellWidget(row,1,self.layerLoad(row,1))
            self.setCellWidget(row,2,self.filtersLoad())
            self.setItem(row,3,QtGui.QTableWidgetItem(""))
            self.setCellWidget(row,4,self.layerLoad(row,4))
        print self.cellWidget(19,1)
        print self.cellWidget(19,4).row,self.cellWidget(19,4).column

    def layerLoad(self):
        layerItem=QtGui.QComboBox()
        for layer in self.layerList:
            layerItem.addItem(layer)
        layerItem.insertItem(0,"Select")
        layerItem.setCurrentIndex(0)
        #layerItem.activated.connect(self.signalMapper.map)
        #layerItem.row=row
        #layerItem.column=col
        #print layerItem.row,layerItem.column,layerItem
        #self.signalMapper.setMapping(layerItem, layerItem)
        return layerItem

    def fieldsLoad(self,row,col):
        fieldItem=QtGui.QComboBox()
        for field in self.layerQueryFields:
            fieldItem.addItem(field)
        fieldItem.insertItem(0,"Select")
        fieldItem.setCurrentIndex(0)
        fieldItem.activated.connect(self.signalMapper.map)
        fieldItem.row=row
        fieldItem.column=col
        #print layerItem.row,layerItem.column,layerItem
        self.signalMapper.setMapping(fieldItem, fieldItem)
        return fieldItem


    def attributefiltersLoad(self):
        filterItem=QtGui.QComboBox()
        filterItem.addItem("=")
        filterItem.addItem("<>")
        filterItem.addItem(">")
        filterItem.addItem("<")
        filterItem.addItem(">=")
        filterItem.addItem("<=")
        filterItem.insertItem(0,"Select")
        filterItem.setCurrentIndex(0)
        return filterItem

    def spatialfiltersLoad(self):
        filterItem=QtGui.QComboBox()
        filterItem.addItem("ST_Within")
        filterItem.addItem("ST_Contains")
        filterItem.addItem("ST_Covers")
        filterItem.addItem("ST_Equals")
        filterItem.addItem("ST_Touches")
        filterItem.addItem("ST_Overlaps")
        filterItem.addItem("ST_Intersects")
        filterItem.addItem("ST_Disjoint")
        filterItem.addItem("ST_Crosses")
        filterItem.insertItem(0,"Select")
        filterItem.setCurrentIndex(0)
        return filterItem

    def testSignal(self,v1,v2):
        print "catch:", v1,v2

    def actionCell(self,row,col):
        controlItem=QtGui.QComboBox()
        controlItem.addItem("")
        controlItem.addItem("Attribute filter")
        controlItem.addItem("Spatial filter")
        controlItem.addItem("")
        controlItem.addItem("AND")
        controlItem.addItem("OR")
        controlItem.addItem("NOT")
        controlItem.addItem("(")
        controlItem.addItem(")")
        controlItem.addItem("")
        controlItem.addItem("Delete")
        controlItem.addItem("Insert")
        controlItem.setCurrentIndex(0)
        controlItem.activated.connect(self.signalMapper.map)
        controlItem.setMaxVisibleItems(20)
        controlItem.row=row
        controlItem.column=col
        self.signalMapper.setMapping(controlItem, controlItem)
        return controlItem

    def actionFilterCell(self,row,col):
        controlItem=QtGui.QComboBox()
        controlItem.addItem("")
        controlItem.addItem("Attribute filter")
        controlItem.addItem("Spatial filter")
        controlItem.addItem("NOT")
        controlItem.addItem("(")
        controlItem.addItem("")
        controlItem.addItem("Delete")
        controlItem.addItem("Insert")
        controlItem.insertItem(0,"Select filter")
        controlItem.setCurrentIndex(0)
        controlItem.activated.connect(self.signalMapper.map)
        controlItem.row=row
        controlItem.column=col
        self.signalMapper.setMapping(controlItem, controlItem)
        return controlItem

    def actionBoolCell(self,row,col):
        controlItem=QtGui.QComboBox()
        controlItem.addItem("")
        controlItem.addItem("AND")
        controlItem.addItem("OR")
        controlItem.addItem(")")
        controlItem.addItem("")
        controlItem.addItem("Delete")
        controlItem.addItem("Insert")
        controlItem.insertItem(0,"Select filter")
        controlItem.setCurrentIndex(0)
        controlItem.activated.connect(self.signalMapper.map)
        controlItem.row=row
        controlItem.column=col
        self.signalMapper.setMapping(controlItem, controlItem)
        return controlItem
        
    def groupFilterCell(self,row,col):
        controlItem=QtGui.QComboBox()
        controlItem.addItem("")
        controlItem.addItem("Attribute filter")
        controlItem.addItem("Spatial filter")
        controlItem.addItem("AND/OR")
        controlItem.addItem("NOT/()")
        controlItem.addItem("")
        controlItem.addItem("Delete")
        controlItem.insertItem(0,"Select filter")
        controlItem.setCurrentIndex(0)
        controlItem.activated.connect(self.signalMapper.map)
        controlItem.row=row
        controlItem.column=col
        self.signalMapper.setMapping(controlItem, controlItem)
        return controlItem


    def boolLoad(self,predef):
        boolItem=QtGui.QComboBox()
        boolItem.addItem("AND")
        boolItem.addItem("OR")
        boolItem.addItem(")")
        if boolItem.findText(predef)== -1:
            boolItem.insertItem(0,"Select")
            boolItem.setCurrentIndex(0)
        else:
            boolItem.setCurrentIndex(boolItem.findText(predef))
        return boolItem

    def groupLoad(self,predef):
        groupItem=QtGui.QComboBox()
        groupItem.addItem("NOT")
        groupItem.addItem("(")
        if groupItem.findText(predef) == -1:
            groupItem.insertItem(0,"Select")
            groupItem.setCurrentIndex(0)
        else:
            groupItem.setCurrentIndex(groupItem.findText(predef))
        return groupItem

    def oneValueLoad(self,value):
        item = QtGui.QComboBox()
        item.addItem(value)
        return item

    def valueLoad(self):
        valueItem = QtGui.QComboBox()
        valueItem.setEditable(True)
        return valueItem
        
    def uniqueValuesLoad(self,row,col,uniqueValueList):
        valueItem = self.cellWidget(row,col)
        valueItem.clear()
        for value in uniqueValueList:
            try :
                valueItem.addItem(value.encode('utf8','ignore'))
            except:
                valueItem.addItem(str(value))
        valueItem.insertItem(0,"Select or type")
        valueItem.setCurrentIndex(0)
        
    def delRow(self,row):
        for oldRow in range(row,self.rowCount()):
            for col in range(0,3):
                try:
                    self.cellWidget(oldRow,col).row = oldRow-1
                except:
                    pass
        self.removeRow(row)
        self.setCellWidget(self.rowCount()-1,0,self.actionCell(self.rowCount()-1,0))

    def insRow(self,row):
        for oldRow in range(row,self.rowCount()):
            for col in range(0,3):
                try:
                    self.cellWidget(oldRow,col).row = oldRow+1
                except:
                    pass
        self.insertRow(row)
        self.setCellWidget(row,0,self.actionCell(row,0))

    def testIfSintaxOk(self):
        res= None
        parOpen=0
        parClosed=0
        previous = "AND/OR"
        for row in range(0,self.rowCount()-1):
            if self.cellWidget(row,1).currentText() == '(': 
                if previous in ['QUERY',')']:
                    print "malformed: ("
                    return None
                parOpen += 1
                previous = "("
            elif self.cellWidget(row,1).currentText() == ')': 
                if previous in ['AND/OR','(']:
                    print "malformed: )"
                    return None
                parClosed += 1
                previous = ")"
            elif self.cellWidget(row,1).currentText() == 'NOT': 
                if previous in ['QUERY',')','(']:
                    print "malformed: )"
                    return None
                parClosed += 1
                previous = "NOT"
            elif self.cellWidget(row,2).currentText() in ['=','>','<','>=','<=','<>'] or self.cellWidget(row,2).currentText()[:2]=="ST":
                if previous == "QUERY":
                    print "malformed: QUERY"
                    return None
                previous = "QUERY"
            elif self.cellWidget(row,1).currentText() == 'AND' or self.cellWidget(row,1).currentText() == 'OR':
                if previous == "AND/OR":
                    print "malformed: AND/OR"
                    return None
                previous = "AND/OR"
            for column in range (1,3):
                if self.cellWidget(row,column).currentText()[:6] == 'Select':
                    print "malformed: Select"
                    return None
        if parOpen != parClosed:
            print "malformed: ()"
            return None
        return True


    def getWhereStatement(self):
        whereStatement = ""
        if not(self.testIfSintaxOk() and self.rowCount()>1):
            return ""
        for row in range(0,self.rowCount()-1):
            if self.cellWidget(row,2).currentText() in ['=','>','<','>=','<=','<>']:
                fType = self.PSQL.getFieldsType(self.layerQuery,self.cellWidget(row,1).currentText())
                fType = fType[:4]
                #print fType
                if ((fType == "char") or (fType == "text") or  (fType == "varc")):
                    value = "'"+self.cellWidget(row,3).currentText()+"'"
                else:
                    value = self.cellWidget(row,3).currentText()
                whereStatement += '"%s"."%s" %s %s ' % (self.layerQuery,self.cellWidget(row,1).currentText(),self.cellWidget(row,2).currentText(),value)
            elif self.cellWidget(row,2).currentText()[:2]=="ST":
                whereStatement += '%s("%s"."%s","%s"."%s") ' % (self.cellWidget(row,2).currentText(),\
                                                                self.layerQuery,\
                                                                self.PSQL.getGeometryField(self.layerQuery),\
                                                                self.cellWidget(row,3).currentText(),\
                                                                self.PSQL.getGeometryField(self.cellWidget(row,3).currentText()))
            else:
                whereStatement += self.cellWidget(row,1).currentText()+" "
        if whereStatement != "": 
            whereStatement = " WHERE " + whereStatement
        return whereStatement



    @QtCore.pyqtSlot(QtGui.QWidget)
    def on_signalMapper_mapped(self,cbox):
        #print "row: {0} column: {1} text: {2}".format(cbox.row,cbox.column,cbox.currentText())
        print cbox.currentText()
        print "ROWS:",self.rowCount()
        nextAction=''
        if cbox.column == 1:
            self.uniqueValuesLoad(cbox.row,3,self.PSQL.getUniqeValues(self.layerQuery,self.cellWidget(cbox.row,1).currentText(),50))
        if cbox.column == 0:
            if cbox.currentText() == "Attribute filter":
                nextAction = "bool"
                self.setCellWidget(cbox.row,1,self.fieldsLoad(cbox.row,1))
                self.setCellWidget(cbox.row,2,self.attributefiltersLoad())
                self.setCellWidget(cbox.row,3,self.valueLoad())
            elif cbox.currentText() == "Spatial filter":
                nextAction = "bool"
                self.setCellWidget(cbox.row,1,self.oneValueLoad(self.layerQuery))
                self.setCellWidget(cbox.row,2,self.spatialfiltersLoad())
                self.setCellWidget(cbox.row,3,self.layerLoad())
            elif cbox.currentText() == "OR":
                nextAction = "filter/group"
                self.setCellWidget(cbox.row,1,self.boolLoad('OR'))
                self.setCellWidget(cbox.row,2,self.oneValueLoad(""))
                self.setCellWidget(cbox.row,3,self.oneValueLoad(""))
            elif cbox.currentText() == "AND":
                nextAction = "filter/group"
                self.setCellWidget(cbox.row,1,self.boolLoad('AND'))
                self.setCellWidget(cbox.row,2,self.oneValueLoad(""))
                self.setCellWidget(cbox.row,3,self.oneValueLoad(""))
            elif cbox.currentText() == "NOT":
                nextAction = "filter/group"
                self.setCellWidget(cbox.row,1,self.groupLoad('NOT'))
                self.setCellWidget(cbox.row,2,self.oneValueLoad(""))
                self.setCellWidget(cbox.row,3,self.oneValueLoad(""))
            elif cbox.currentText() == "(":
                nextAction = "filter/group"
                self.setCellWidget(cbox.row,1,self.groupLoad('('))
                self.setCellWidget(cbox.row,2,self.oneValueLoad(""))
                self.setCellWidget(cbox.row,3,self.oneValueLoad(""))
            elif cbox.currentText() == ")":
                nextAction = "filter/group"
                self.setCellWidget(cbox.row,1,self.groupLoad(')'))
                self.setCellWidget(cbox.row,2,self.oneValueLoad(""))
                self.setCellWidget(cbox.row,3,self.oneValueLoad(""))
            elif cbox.currentText() == "Delete":
                if cbox.row != (self.rowCount()-1):
                    self.delRow(cbox.row)
            elif cbox.currentText() == "Insert":
                if cbox.row != (self.rowCount()-1):
                    self.insRow(cbox.row)
            elif cbox.currentText() == "":
                if self.testIfSintaxOk(): print "wellformed query:"
                else: print "malformed query:"
                print self.getWhereStatement()
                return None
            if cbox.row == (self.rowCount()-1):
                self.insertRow((self.rowCount()))
                if nextAction == "filter/group":
                    self.setCellWidget(self.rowCount()-1,0,self.actionFilterCell(self.rowCount()-1,0))
                elif nextAction == "bool":
                    self.setCellWidget(self.rowCount()-1,0,self.actionBoolCell(self.rowCount()-1,0))
                cbox.removeItem(0)
                cbox.setCurrentIndex(0)
            else:
                cbox.setCurrentIndex(0)
                #cbox.setItemText(0,"")
        print self.getWhereStatement()