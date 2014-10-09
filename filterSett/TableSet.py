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

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class tableSet():

    def __init__(self,twg,layerList):
        self.twg = twg
        self.layerList = layerList
        self.twg.clearContents()
        self.twg.setRowCount(20)
        self.twg.setColumnCount(5)
        for row in range (0,20):
            self.twg.setCellWidget.(row,1,self.junctionLoad())
            self.twg.setCellWidget.(row,1,self.layerLoad())
            self.twg.setCellWidget.(row,2,self.filtersLoad())
            self.twg.setItem(row,3,QTableWidgetItem(""))
            self.twg.setCellWidget.(row,4,self.layerLoad())

    def layerLoad(self):
        layerItem=QComboBox()
        for layer in self.layerList:
            layerItem.addItem(layer)
        layerItem.insertItem(0,"")
        layerItem.setCurrentIndex(0)
        return layerItem

    def filtersLoad(self):
        filterItem=QComboBox()
        filterItem.addItem("=")
        filterItem.addItem("<>")
        filterItem.addItem(">")
        filterItem.addItem("<")
        filterItem.addItem(">=")
        filterItem.addItem("<=")
        filterItem.addItem("ST_Within")
        filterItem.addItem("ST_Contains")
        filterItem.addItem("ST_Covers")
        filterItem.addItem("ST_Equals")
        filterItem.addItem("ST_Touches")
        filterItem.addItem("ST_Overlaps")
        filterItem.addItem("ST_Intersects")
        filterItem.addItem("ST_Disjoint")
        filterItem.addItem("ST_Crosses")
        filterItem.insertItem(0,"")
        filterItem.setCurrentIndex(0)
        return filterItem

    def junctionRow(self,tableList,row):
        controlItem=QComboBox()
        controlItem.addItem("AND")
        controlItem.addItem("OR")
        controlItem.addItem("NOT")
        controlItem.addItem("(")
        controlItem.addItem(")")
        controlItem.insertItem(0,"")
        controlItem.setCurrentIndex(0)
        return controlItem