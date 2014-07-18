from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
from qgis.core import *

import os.path

class PSQL:

    def __init__(self,iface):
        self.iface = iface
        self.schema = ""

    def getConnections(self):
        s = QSettings() 
        s.beginGroup("PostgreSQL/connections")
        currentConnections = s.childGroups()
        #print "connections: ",currentConnections
        s.endGroup()
        return currentConnections


    def setConnection(self,conn):
        s = QSettings()
        s.beginGroup("PostgreSQL/connections/"+conn)
        currentKeys = s.childKeys()
        #print "keys: ", currentKeys
        self.PSQLDatabase=s.value("database", "" )
        self.PSQLHost=s.value("host", "" )
        self.PSQLUsername=s.value("username", "" )
        self.PSQLPassword=s.value("password", "" )
        self.PSQLPort=s.value("port", "" )
        self.PSQLService=s.value("service", "" )
        s.endGroup()
        #print self.PSQLDatabase,self.PSQLService,self.PSQLHost,self.PSQLPort,self.PSQLUsername,self.PSQLPassword
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setHostName(self.PSQLHost)
        self.db.setPort(int(self.PSQLPort))
        self.db.setDatabaseName(self.PSQLDatabase)
        self.db.setUserName(self.PSQLUsername)
        self.db.setPassword(self.PSQLPassword)
        ok = self.db.open()
        if not ok:
            error = "Database Error: %s" % self.db.lastError().text()
            QMessageBox.information(None, "DB ERROR:", error)
        else:
            error=""
        #print error
        return error

    def setSchema(self,schema):
        self.schema = schema

    def getLayers(self):
        sql="select table_name from information_schema.tables where table_schema='%s';" % self.schema 
        query = self.db.exec_(sql)
        layers=[]
        exclusionList = ["spatial_ref_sys","geography_columns","geometry_columns","raster_columns","raster_overviews"]
        while (query.next()):
            if not query.value(0) in exclusionList : layers.append(query.value(0))
        sql="SELECT matviewname FROM pg_matviews where schemaname='%s';"  % self.schema
        query = self.db.exec_(sql)
        while (query.next()):
            layers.append(str(query.value(0)))
        layers.sort()
        return layers

    def testIfFidExist(self,layer):
        fields=self.getFieldsContent(layer)
        test = None
        for f in fields:
            if (f == "ogc_fid"):
                test = True
        return test

    def refreshMaterializedView(self,mView):
        sql = "REFRESH MATERIALIZED VIEW '%s'" % mView
        return self.submitCommand(sql)

    def deleteLayer(self,layer):
        if self.isTable(layer): sql = 'DROP TABLE "%s"' % layer
        elif self.isView (layer): sql = 'DROP VIEW "%s"' % layer
        elif self.isMaterializedView (layer): sql = 'DROP MATERIALIZED VIEW "%s"' % layer
        else: sql =""
        return self.submitCommand(sql)

    def getFieldsContent(self,layer):
        sql="SELECT column_name FROM information_schema.columns WHERE table_name='%s';" % layer
        query = self.db.exec_(sql)
        fields=[]
        while (query.next()):
            fields.append(str(query.value(0)))
        if fields==[]:
            sql="SELECT attname, typname ,relname FROM pg_attribute a JOIN pg_class c on a.attrelid = c.oid JOIN pg_type t on a.atttypid = t.oid WHERE relname = '%s' and attnum >= 1;" % layer
            #print sql
            query = self.db.exec_(sql)
            while (query.next()):
                fields.append(str(query.value(0)))
            #print fields
        return fields

    def getFieldsType(self,layer,field):
        sql = "SELECT typname FROM pg_attribute a JOIN pg_class c on a.attrelid = c.oid JOIN pg_type t on a.atttypid = t.oid WHERE relname = '%s' and attname = '%s'" % (layer,field)
        query = self.db.exec_(sql)
        query.next()
        res = str(query.value(0))
        #print res
        return res

    def getUniqeValues(self,layer,field,range):
        sql = 'SELECT DISTINCT %s FROM "%s"' % (field,layer)
        query = self.db.exec_(sql)
        values = []
        conta = 0
        while (query.next()):
            values.append(str(query.value(0)))
            if conta == range:
                return values
                pass
            conta = conta+1
        return values

    def getSchemas(self):
        sql="select schema_name from information_schema.schemata where schema_name <> 'information_schema' and schema_name !~ E'^pg_'"
        query = self.db.exec_(sql)
        schemas=[]
        while (query.next()):
            schemas.append(query.value(0))
        return schemas


    def submitQuery(self,sql):
        query = QSqlQuery(self.db)
        query.exec_(sql)
        result={}
        if not query:
            result["error"] = "Database Error: %s" % db.lastError().text()
            result["result"] = []
            QMessageBox.information(None, "SQL ERROR:", resultQuery) 
        else:
            result["error"] = ""
            rows=[[]]
            #void=[]
            #rows.append[void]
            while (query.next()):
                fields=[]
                count = 0
                query.value(count)
                for k in range(0,query.record().count()):
                    try:
                        fields.append(query.value(k).toString())
                    except AttributeError:
                        fields.append(str(query.value(k)))
                    if rows[0] == []:
                        fieldNames=[]
                        for n in range(0,query.record().count()):
                            fieldNames.append(query.record().fieldName(n))
                        rows[0]=fieldNames
                #print rows
                rows += [fields]
            result["result"] = rows
        #print result
        return result

    def submitCommand(self,sql):
        query = QSqlQuery(self.db)
        query.exec_(sql)
        if query.lastError().text() != " ":
            self.queryLogger(sql)
        return query.lastError().text()

    def isTable(self,tName):
        sql = "SELECT tablename FROM pg_catalog.pg_tables where schemaname = '%s' and tablename = '%s'" % (self.schema,tName)
        query = QSqlQuery(self.db)
        query.exec_(sql)
        query.first()
        return query.isValid()

    def isView(self,vName):
        sql = "SELECT viewname FROM pg_catalog.pg_views where schemaname = '%s' and viewname = '%s'" % (self.schema,vName)
        #print sql
        query = QSqlQuery(self.db)
        query.exec_(sql)
        query.first()
        return query.isValid()

    def isMaterializedView(self,vName):
        sql = sql="SELECT matviewname FROM pg_matviews where schemaname='%s'  and matviewname = '%s'" % (self.schema,vName)
        query = QSqlQuery(self.db)
        query.exec_(sql)
        query.first()
        return query.isValid()

    def loadView(self,layer,GeomField,KeyField):
        uri = QgsDataSourceURI()
        uri.setConnection(self.PSQLHost,self.PSQLPort,self.PSQLDatabase,self.PSQLUsername,self.PSQLPassword)
        uri.setDataSource("public",layer,GeomField,"",KeyField)
        vlayer = QgsVectorLayer(uri.uri(), layer, "postgres")
        if vlayer.isValid():
            QgsMapLayerRegistry.instance().addMapLayer(vlayer,True)
        else:
            QMessageBox.information(None, "LAYER ERROR:", "The layer %s is not valid" % layer)
    
    def loadSql(self,layerName,sql,GeomField,KeyField):
        uri = QgsDataSourceURI()
        uri.setConnection(self.PSQLHost,self.PSQLPort,self.PSQLDatabase,self.PSQLUsername,self.PSQLPassword)
        uri.setDataSource("","("+sql+")",GeomField,"",KeyField)
        vlayer = QgsVectorLayer(uri.uri(), layerName, "postgres")
        if vlayer.isValid():
            QgsMapLayerRegistry.instance().addMapLayer(vlayer,True)
            self.queryLogger(sql)
        else:
            QMessageBox.information(None, "LAYER ERROR:", "The layer %s is not valid" % layerName)
    
    def queryLogger (self,sql):
        out_file = open(os.path.join(os.path.dirname(__file__),"validSql.log"),"a")
        out_file.write(sql+"\n")
        out_file.close()
    
    def tableResultGen(self,tableName,sql,tableSlot):
        if sql != "":
            res=self.submitQuery(sql)
        else:
            res=self.submitQuery('SELECT * FROM "%s"' % tableName)
        if res["result"] != []:
            tab=res["result"]
            print tab[0]
            print len(tab[0])
            tableSlot.setColumnCount(len(tab[0]))
            tableSlot.setRowCount(len(tab)-1)
            #add field type to field labels
            if tableName != "":
                for column in range(0,len(tab[0])):
                    tab[0][column] += "\n" + self.getFieldsType(tableName,tab[0][column])
            tableSlot.setHorizontalHeaderLabels(tab[0])
            for column in range(0,len(tab[0])):
                for row in range(1,len(tab)):
                    try:
                        item = unicode(tab[row][column], errors='replace')
                    except TypeError:
                        item = str(tab[row][column])
                    if item != None:
                        tableSlot.setItem(row-1, column, QTableWidgetItem(item))