# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_postgisquerybuilder.ui'
#
# Created: Mon May 26 13:37:26 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_postgisQueryBuilder(object):
    def setupUi(self, postgisQueryBuilder):
        postgisQueryBuilder.setObjectName(_fromUtf8("postgisQueryBuilder"))
        postgisQueryBuilder.resize(639, 363)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(postgisQueryBuilder.sizePolicy().hasHeightForWidth())
        postgisQueryBuilder.setSizePolicy(sizePolicy)
        self.ButtonReset = QtGui.QPushButton(postgisQueryBuilder)
        self.ButtonReset.setGeometry(QtCore.QRect(440, 330, 91, 25))
        self.ButtonReset.setObjectName(_fromUtf8("ButtonReset"))
        self.ButtonClose = QtGui.QPushButton(postgisQueryBuilder)
        self.ButtonClose.setGeometry(QtCore.QRect(540, 330, 90, 25))
        self.ButtonClose.setObjectName(_fromUtf8("ButtonClose"))
        self.tabWidget = QtGui.QTabWidget(postgisQueryBuilder)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 621, 311))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.ConnectionTab = QtGui.QWidget()
        self.ConnectionTab.setObjectName(_fromUtf8("ConnectionTab"))
        self.KEYFIELDLabel = QtGui.QLabel(self.ConnectionTab)
        self.KEYFIELDLabel.setGeometry(QtCore.QRect(10, 55, 181, 16))
        self.KEYFIELDLabel.setObjectName(_fromUtf8("KEYFIELDLabel"))
        self.GEOMETRYFIELDLabel = QtGui.QLabel(self.ConnectionTab)
        self.GEOMETRYFIELDLabel.setGeometry(QtCore.QRect(10, 102, 171, 16))
        self.GEOMETRYFIELDLabel.setObjectName(_fromUtf8("GEOMETRYFIELDLabel"))
        self.GEOMETRYFIELD = QtGui.QLineEdit(self.ConnectionTab)
        self.GEOMETRYFIELD.setGeometry(QtCore.QRect(10, 121, 180, 20))
        self.GEOMETRYFIELD.setObjectName(_fromUtf8("GEOMETRYFIELD"))
        self.KEYFIELD = QtGui.QLineEdit(self.ConnectionTab)
        self.KEYFIELD.setGeometry(QtCore.QRect(10, 74, 180, 20))
        self.KEYFIELD.setObjectName(_fromUtf8("KEYFIELD"))
        self.PSQLConnectionLabel = QtGui.QLabel(self.ConnectionTab)
        self.PSQLConnectionLabel.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.PSQLConnectionLabel.setObjectName(_fromUtf8("PSQLConnectionLabel"))
        self.PSQLConnection = QtGui.QComboBox(self.ConnectionTab)
        self.PSQLConnection.setGeometry(QtCore.QRect(10, 29, 180, 20))
        self.PSQLConnection.setObjectName(_fromUtf8("PSQLConnection"))
        self.DBSchema = QtGui.QComboBox(self.ConnectionTab)
        self.DBSchema.setGeometry(QtCore.QRect(10, 164, 180, 22))
        self.DBSchema.setObjectName(_fromUtf8("DBSchema"))
        self.DBSchemaLabel = QtGui.QLabel(self.ConnectionTab)
        self.DBSchemaLabel.setGeometry(QtCore.QRect(10, 145, 181, 16))
        self.DBSchemaLabel.setObjectName(_fromUtf8("DBSchemaLabel"))
        self.LayerList = QtGui.QListWidget(self.ConnectionTab)
        self.LayerList.setGeometry(QtCore.QRect(210, 30, 391, 221))
        self.LayerList.setObjectName(_fromUtf8("LayerList"))
        self.RefreshButton = QtGui.QPushButton(self.ConnectionTab)
        self.RefreshButton.setGeometry(QtCore.QRect(510, 257, 90, 23))
        self.RefreshButton.setObjectName(_fromUtf8("RefreshButton"))
        self.AddToMapButton = QtGui.QPushButton(self.ConnectionTab)
        self.AddToMapButton.setGeometry(QtCore.QRect(310, 257, 90, 23))
        self.AddToMapButton.setObjectName(_fromUtf8("AddToMapButton"))
        self.DeleteButton = QtGui.QPushButton(self.ConnectionTab)
        self.DeleteButton.setGeometry(QtCore.QRect(410, 257, 90, 23))
        self.DeleteButton.setObjectName(_fromUtf8("DeleteButton"))
        self.GetInfoButton = QtGui.QPushButton(self.ConnectionTab)
        self.GetInfoButton.setGeometry(QtCore.QRect(210, 257, 90, 23))
        self.GetInfoButton.setObjectName(_fromUtf8("GetInfoButton"))
        self.tabWidget.addTab(self.ConnectionTab, _fromUtf8(""))
        self.DefinitionTab = QtGui.QWidget()
        self.DefinitionTab.setObjectName(_fromUtf8("DefinitionTab"))
        self.SPATIALRELNOT = QtGui.QCheckBox(self.DefinitionTab)
        self.SPATIALRELNOT.setGeometry(QtCore.QRect(310, 260, 50, 18))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SPATIALRELNOT.sizePolicy().hasHeightForWidth())
        self.SPATIALRELNOT.setSizePolicy(sizePolicy)
        self.SPATIALRELNOT.setMaximumSize(QtCore.QSize(50, 16777215))
        self.SPATIALRELNOT.setObjectName(_fromUtf8("SPATIALRELNOT"))
        self.CONDITIONLabel = QtGui.QLabel(self.DefinitionTab)
        self.CONDITIONLabel.setGeometry(QtCore.QRect(310, 241, 151, 16))
        self.CONDITIONLabel.setObjectName(_fromUtf8("CONDITIONLabel"))
        self.OPERATOR = QtGui.QComboBox(self.DefinitionTab)
        self.OPERATOR.setGeometry(QtCore.QRect(224, 260, 81, 20))
        self.OPERATOR.setObjectName(_fromUtf8("OPERATOR"))
        self.BUFFERRADIUSLabel = QtGui.QLabel(self.DefinitionTab)
        self.BUFFERRADIUSLabel.setGeometry(QtCore.QRect(5, 241, 281, 16))
        self.BUFFERRADIUSLabel.setObjectName(_fromUtf8("BUFFERRADIUSLabel"))
        self.SPATIALRELLabel = QtGui.QLabel(self.DefinitionTab)
        self.SPATIALRELLabel.setGeometry(QtCore.QRect(5, 241, 281, 16))
        self.SPATIALRELLabel.setObjectName(_fromUtf8("SPATIALRELLabel"))
        self.CONDITION = QtGui.QComboBox(self.DefinitionTab)
        self.CONDITION.setGeometry(QtCore.QRect(310, 260, 151, 20))
        self.CONDITION.setEditable(True)
        self.CONDITION.setObjectName(_fromUtf8("CONDITION"))
        self.OPERATORLabel = QtGui.QLabel(self.DefinitionTab)
        self.OPERATORLabel.setGeometry(QtCore.QRect(224, 241, 98, 16))
        self.OPERATORLabel.setObjectName(_fromUtf8("OPERATORLabel"))
        self.FIELDLabel = QtGui.QLabel(self.DefinitionTab)
        self.FIELDLabel.setGeometry(QtCore.QRect(5, 241, 201, 16))
        self.FIELDLabel.setObjectName(_fromUtf8("FIELDLabel"))
        self.FIELD = QtGui.QComboBox(self.DefinitionTab)
        self.FIELD.setGeometry(QtCore.QRect(5, 260, 214, 20))
        self.FIELD.setObjectName(_fromUtf8("FIELD"))
        self.BUFFERRADIUS = QtGui.QLineEdit(self.DefinitionTab)
        self.BUFFERRADIUS.setGeometry(QtCore.QRect(5, 260, 170, 20))
        self.BUFFERRADIUS.setObjectName(_fromUtf8("BUFFERRADIUS"))
        self.SPATIALREL = QtGui.QComboBox(self.DefinitionTab)
        self.SPATIALREL.setGeometry(QtCore.QRect(5, 260, 300, 20))
        self.SPATIALREL.setObjectName(_fromUtf8("SPATIALREL"))
        self.LAYERb = QtGui.QComboBox(self.DefinitionTab)
        self.LAYERb.setGeometry(QtCore.QRect(310, 92, 300, 20))
        self.LAYERb.setObjectName(_fromUtf8("LAYERb"))
        self.fieldsListB = QtGui.QListWidget(self.DefinitionTab)
        self.fieldsListB.setGeometry(QtCore.QRect(310, 115, 300, 121))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldsListB.sizePolicy().hasHeightForWidth())
        self.fieldsListB.setSizePolicy(sizePolicy)
        self.fieldsListB.setMinimumSize(QtCore.QSize(0, 0))
        self.fieldsListB.setMaximumSize(QtCore.QSize(16777215, 25000))
        self.fieldsListB.setObjectName(_fromUtf8("fieldsListB"))
        self.LAYERaLabel = QtGui.QLabel(self.DefinitionTab)
        self.LAYERaLabel.setGeometry(QtCore.QRect(5, 75, 151, 16))
        self.LAYERaLabel.setObjectName(_fromUtf8("LAYERaLabel"))
        self.fieldsListA = QtGui.QListWidget(self.DefinitionTab)
        self.fieldsListA.setGeometry(QtCore.QRect(5, 115, 300, 121))
        self.fieldsListA.setMinimumSize(QtCore.QSize(150, 0))
        self.fieldsListA.setObjectName(_fromUtf8("fieldsListA"))
        self.LAYERbLabel = QtGui.QLabel(self.DefinitionTab)
        self.LAYERbLabel.setGeometry(QtCore.QRect(310, 75, 161, 16))
        self.LAYERbLabel.setObjectName(_fromUtf8("LAYERbLabel"))
        self.LAYERa = QtGui.QComboBox(self.DefinitionTab)
        self.LAYERa.setGeometry(QtCore.QRect(5, 92, 300, 20))
        self.LAYERa.setObjectName(_fromUtf8("LAYERa"))
        self.QueryType = QtGui.QComboBox(self.DefinitionTab)
        self.QueryType.setGeometry(QtCore.QRect(5, 10, 211, 20))
        self.QueryType.setMaxVisibleItems(20)
        self.QueryType.setObjectName(_fromUtf8("QueryType"))
        self.Helper = QtGui.QLabel(self.DefinitionTab)
        self.Helper.setGeometry(QtCore.QRect(229, 10, 381, 61))
        self.Helper.setAutoFillBackground(False)
        self.Helper.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Helper.setText(_fromUtf8(""))
        self.Helper.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Helper.setWordWrap(True)
        self.Helper.setObjectName(_fromUtf8("Helper"))
        self.ButtonHelp = QtGui.QPushButton(self.DefinitionTab)
        self.ButtonHelp.setGeometry(QtCore.QRect(520, 258, 90, 25))
        self.ButtonHelp.setObjectName(_fromUtf8("ButtonHelp"))
        self.label = QtGui.QLabel(self.DefinitionTab)
        self.label.setGeometry(QtCore.QRect(5, 34, 131, 16))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.DISTANCE = QtGui.QLineEdit(self.DefinitionTab)
        self.DISTANCE.setGeometry(QtCore.QRect(100, 260, 113, 20))
        self.DISTANCE.setObjectName(_fromUtf8("DISTANCE"))
        self.DISTANCELabel = QtGui.QLabel(self.DefinitionTab)
        self.DISTANCELabel.setGeometry(QtCore.QRect(100, 241, 151, 16))
        self.DISTANCELabel.setObjectName(_fromUtf8("DISTANCELabel"))
        self.DISTANCEOPLabel = QtGui.QLabel(self.DefinitionTab)
        self.DISTANCEOPLabel.setGeometry(QtCore.QRect(5, 241, 98, 16))
        self.DISTANCEOPLabel.setObjectName(_fromUtf8("DISTANCEOPLabel"))
        self.DISTANCEOP = QtGui.QComboBox(self.DefinitionTab)
        self.DISTANCEOP.setGeometry(QtCore.QRect(5, 260, 81, 20))
        self.DISTANCEOP.setObjectName(_fromUtf8("DISTANCEOP"))
        self.tabWidget.addTab(self.DefinitionTab, _fromUtf8(""))
        self.QueryTab = QtGui.QWidget()
        self.QueryTab.setObjectName(_fromUtf8("QueryTab"))
        self.AddToMap = QtGui.QCheckBox(self.QueryTab)
        self.AddToMap.setGeometry(QtCore.QRect(110, 253, 116, 18))
        self.AddToMap.setChecked(True)
        self.AddToMap.setObjectName(_fromUtf8("AddToMap"))
        self.ButtonRun = QtGui.QPushButton(self.QueryTab)
        self.ButtonRun.setGeometry(QtCore.QRect(5, 250, 90, 25))
        self.ButtonRun.setObjectName(_fromUtf8("ButtonRun"))
        self.checkMaterialized = QtGui.QCheckBox(self.QueryTab)
        self.checkMaterialized.setGeometry(QtCore.QRect(90, 10, 111, 18))
        self.checkMaterialized.setObjectName(_fromUtf8("checkMaterialized"))
        self.QueryName = QtGui.QLineEdit(self.QueryTab)
        self.QueryName.setGeometry(QtCore.QRect(199, 10, 411, 20))
        self.QueryName.setObjectName(_fromUtf8("QueryName"))
        self.checkCreateView = QtGui.QCheckBox(self.QueryTab)
        self.checkCreateView.setGeometry(QtCore.QRect(5, 10, 81, 18))
        self.checkCreateView.setObjectName(_fromUtf8("checkCreateView"))
        self.QueryResult = QtGui.QTextEdit(self.QueryTab)
        self.QueryResult.setGeometry(QtCore.QRect(5, 40, 605, 201))
        self.QueryResult.setObjectName(_fromUtf8("QueryResult"))
        self.tabWidget.addTab(self.QueryTab, _fromUtf8(""))
        self.TableTab = QtGui.QWidget()
        self.TableTab.setAccessibleName(_fromUtf8(""))
        self.TableTab.setObjectName(_fromUtf8("TableTab"))
        self.TableResult = QtGui.QTableWidget(self.TableTab)
        self.TableResult.setGeometry(QtCore.QRect(5, 5, 605, 275))
        self.TableResult.setObjectName(_fromUtf8("TableResult"))
        self.TableResult.setColumnCount(0)
        self.TableResult.setRowCount(0)
        self.TableResult.horizontalHeader().setMinimumSectionSize(25)
        self.TableResult.verticalHeader().setDefaultSectionSize(25)
        self.tabWidget.addTab(self.TableTab, _fromUtf8(""))

        self.retranslateUi(postgisQueryBuilder)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(postgisQueryBuilder)

    def retranslateUi(self, postgisQueryBuilder):
        postgisQueryBuilder.setWindowTitle(_translate("postgisQueryBuilder", "postgisQueryBuilder", None))
        self.ButtonReset.setText(_translate("postgisQueryBuilder", "reset form", None))
        self.ButtonClose.setText(_translate("postgisQueryBuilder", "close", None))
        self.KEYFIELDLabel.setText(_translate("postgisQueryBuilder", "Key field", None))
        self.GEOMETRYFIELDLabel.setText(_translate("postgisQueryBuilder", "Geometry field", None))
        self.PSQLConnectionLabel.setText(_translate("postgisQueryBuilder", "Postgresql connection", None))
        self.DBSchemaLabel.setText(_translate("postgisQueryBuilder", "Schema", None))
        self.RefreshButton.setText(_translate("postgisQueryBuilder", "Refresh", None))
        self.AddToMapButton.setText(_translate("postgisQueryBuilder", "Add to map", None))
        self.DeleteButton.setText(_translate("postgisQueryBuilder", "Delete", None))
        self.GetInfoButton.setText(_translate("postgisQueryBuilder", "Get info", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ConnectionTab), _translate("postgisQueryBuilder", "Connection", None))
        self.SPATIALRELNOT.setText(_translate("postgisQueryBuilder", "NOT", None))
        self.CONDITIONLabel.setText(_translate("postgisQueryBuilder", "Condition", None))
        self.BUFFERRADIUSLabel.setText(_translate("postgisQueryBuilder", "Buffer radius", None))
        self.SPATIALRELLabel.setText(_translate("postgisQueryBuilder", "Spatial relationship between LayerA and Layer B", None))
        self.OPERATORLabel.setText(_translate("postgisQueryBuilder", "Operator", None))
        self.FIELDLabel.setText(_translate("postgisQueryBuilder", "Select Field of Layer A", None))
        self.LAYERaLabel.setText(_translate("postgisQueryBuilder", "Layer A", None))
        self.LAYERbLabel.setText(_translate("postgisQueryBuilder", "Layer B", None))
        self.ButtonHelp.setText(_translate("postgisQueryBuilder", "Help ", None))
        self.label.setText(_translate("postgisQueryBuilder", "Query type", None))
        self.DISTANCELabel.setText(_translate("postgisQueryBuilder", "Condition", None))
        self.DISTANCEOPLabel.setText(_translate("postgisQueryBuilder", "Operator", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DefinitionTab), _translate("postgisQueryBuilder", "Definition", None))
        self.AddToMap.setText(_translate("postgisQueryBuilder", "Add to map", None))
        self.ButtonRun.setText(_translate("postgisQueryBuilder", "Run query", None))
        self.checkMaterialized.setText(_translate("postgisQueryBuilder", "Materialized", None))
        self.checkCreateView.setText(_translate("postgisQueryBuilder", "As view", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.QueryTab), _translate("postgisQueryBuilder", "Query", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TableTab), _translate("postgisQueryBuilder", "Table result", None))

