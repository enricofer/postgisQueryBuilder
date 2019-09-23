# -*- coding: utf-8 -*-
"""
/***************************************************************************
 postgisQueryBuilder/querysetbuilder
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
from sqlparse import format

class querySet():

    def __init__(self):
        self.isView = None
        
        self.resetParameters()
        
        self.fieldSet = []
        
        self.spatialRel = {'ST_Within':'help tip','ST_Contains':'help tip','ST_Covers':'help tip','ST_Equals':'help tip','ST_Touches':'help tip','ST_Overlaps':'help tip','ST_Intersects':'help tip','ST_Disjoint':'help tip','ST_Crosses':'help tip',}
        
        self.querySet=\
            {\
            'ST_Centroid':\
            [\
            'Returns the geometric center of geomA.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Centroid.html',\
            ['LAYERa','fieldsListA'],\
            'SELECT [[FIELDSET]],ST_Centroid("[[LAYERa]]".[[GEOMETRYFIELDa]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]" [[WHERE]] [[ORDERBY]]',\
            '_Centroids_of_[[LAYERa]]'\
            ],\
            'ST_PointOnSurface':\
            [\
            'Returns a POINT guaranteed to lie on the surface of geomA.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_PointOnSurface.html',\
            ['LAYERa','fieldsListA'],\
            'SELECT [[FIELDSET]],ST_PointOnSurface("[[LAYERa]]".[[GEOMETRYFIELDa]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]" [[WHERE]] [[ORDERBY]]',\
            '_Points_on_Surfaces_of_[[LAYERa]]'\
            ],\
            'ST_Union 2 layer':\
            [\
            'Returns a geometry that represents the point set union of geomA and geomB.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Union.html',\
            ['LAYERa','SCHEMAb','LAYERb','fieldsListA'],\
            'SELECT [[ONLYGEOMSET]],ST_Union("[[LAYERa]]".[[GEOMETRYFIELDa]],"[[LAYERb]]".[[GEOMETRYFIELDb]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]","[[SCHEMAb]]"."[[LAYERb]] [[WHERE]] [[ORDERBY]]"',\
            '_Union_of_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'ST_Union 1 layer':\
            [\
            'Returns a geometry that represents the point set union of the Geometries in geomA. Geometries are dissolved by attribute selecting dissolving field',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Union.html',\
            ['LAYERa','fieldsListA'],\
            'SELECT [[FIELDSET]],ST_Union("[[LAYERa]]".[[GEOMETRYFIELDa]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]" [[WHERE]] [[ORDERBY]] [[GROUPBYSET]]',\
            '_Union_of_[[LAYERa]]'\
            ],\
            'ST_Difference':\
            [\
            'Returns a geometry that represents that part of geometry A that does not intersect with geometry B.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Difference.html',\
            ['LAYERa','SCHEMAb','LAYERb','fieldsListA'],\
            'SELECT [[FIELDSET]],ST_Difference("[[LAYERa]]".[[GEOMETRYFIELDa]],"[[LAYERb]]".[[GEOMETRYFIELDb]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]","[[SCHEMAb]]"."[[LAYERb]]"  [[WHERE]] [[ORDERBY]]',\
            '_Diff_between_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'ST_Intersection':\
            [\
            'Returns a geometry that represents the shared portion of geomA and geomB. The geography implementation does a transform to geometry to do the intersection and then transform back to WGS84.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Intersection.html',\
            ['LAYERa','SCHEMAb','LAYERb','fieldsListA'],\
            'SELECT [[FIELDSET]],ST_Intersection("[[LAYERa]]".[[GEOMETRYFIELDa]],"[[LAYERb]]".[[GEOMETRYFIELDb]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]","[[SCHEMAb]]"."[[LAYERb]]"  [[WHERE]] [[ORDERBY]]',\
            '_Int_between_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'ST_Buffer':\
            [\
            'For geometry: Returns a geometry that represents all points whose distance from this Geometry is less than or equal to distance. Calculations are in the Spatial Reference System of this Geometry. For geography: Uses a planar transform wrapper.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Buffer.html',\
            ['LAYERa','fieldsListA','BUFFERRADIUS'],\
            'SELECT [[FIELDSET]],ST_Buffer("[[LAYERa]]".[[GEOMETRYFIELDa]],[[BUFFERRADIUS]]::double precision) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]"  [[WHERE]] [[ORDERBY]]',\
            '_Buffer_of_[[LAYERa]]'\
            ],\
            'MEASURE FEATURES':\
            [\
            'Add area and perimeter measurements fields about LayerA geometries. For "geometry" type area is in SRID units. For "geography" area is in square meters.',\
            'http://postgis.org/docs/ST_Area.html',\
            ['LAYERa','fieldsListA'],\
            'SELECT [[FIELDSET]], ST_Area("[[LAYERa]]".[[GEOMETRYFIELDa]]) AS Area_geom, ST_Perimeter("[[LAYERa]]".[[GEOMETRYFIELDa]]) AS Perimeter_geom FROM "[[SCHEMA]]"."[[LAYERa]]" [[WHERE]] [[ORDERBY]]',\
            '_Measurements_of_[[LAYERa]] '\
            ],\
            'FIELDS SELECTION':\
            [\
            'Field subset selection for specified layer ',\
            'http://postgis.org/docs/ST_Area.html',\
            ['LAYERa','fieldsListA'],\
            'SELECT [[FIELDSET]] FROM [[SPATIALFROM]]"[[SCHEMA]]"."[[LAYERa]]" [[WHERE]] [[ORDERBY]]',\
            '_FieldsSubset_of_[[LAYERa]] '\
            ],\
            'VALIDATE GEOMETRIES':\
            [\
            'Mark and report invalid geometries',\
            'http://postgis.net/docs/ST_IsValidDetail.html',\
            ['LAYERa'],\
            'SELECT [[KEYFIELD]],reason(ST_IsValidDetail("[[LAYERa]]".[[GEOMETRYFIELDa]])) AS reason, location(ST_IsValidDetail("[[LAYERa]]".[[GEOMETRYFIELDa]])) AS [[GEOMETRYFIELDa]] FROM "[[SCHEMA]]"."[[LAYERa]]" WHERE NOT ST_IsValid("[[LAYERa]]".[[GEOMETRYFIELDa]])',\
            '_Invalid_geometries_of_[[LAYERa]] '\
            ],\
            'JOIN analytical':\
            [\
            'Returns the result of analytical join of Layer A and Layer B where field A meet field B',\
            'http://www.tutorialspoint.com/postgresql/postgresql_using_joins.htm',\
            ['LAYERa','SCHEMAb','LAYERb','FIELD','FIELDb','JOIN','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]] FROM "[[SCHEMA]]"."[[LAYERa]]" [[JOIN]] "[[SCHEMAb]]"."[[LAYERb]]" ON "[[LAYERa]]".[[FIELD]] = "[[LAYERb]]".[[FIELDb]] [[WHERE]] [[ORDERBY]]',\
            '_analytical_join_of_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'JOIN spatial':\
            [\
            'Returns the result of spatial join of Layer A and Layer B where relationship is true',\
            'http://workshops.boundlessgeo.com/postgis-intro/joins_exercises.html',\
            ['LAYERa','SCHEMAb','LAYERb','SPATIALREL','SPATIALRELNOT','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]] FROM "[[SCHEMA]]"."[[LAYERa]]" INNER JOIN "[[SCHEMAb]]"."[[LAYERb]]" ON [[SPATIALREL]]("[[LAYERa]]".[[GEOMETRYFIELD]],"[[LAYERb]]".[[GEOMETRYFIELD]]) [[WHERE]] [[ORDERBY]]',\
            '_spatial_join_of_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            }

    def setSchema(self,schema):
        self.schemaName = schema

    def setIsView(self,bool):
        self.isView=bool

    def setFIDFIELD(self):
        self.parameters["FIDFIELD"]= "row_number() OVER () AS %s," % (self.getParameter("KEYFIELD"))
    
    def unsetFIDFIELD(self):
        self.parameters["FIDFIELD"]= ""
    
    def setFieldsSet(self,list):
        self.fieldSet = list
    
    def resetParameters(self):
        self.parameters = {"VIEWNAME":"","LAYERa":"","SCHEMAb":"","LAYERb":"","GEOMETRYFIELDa":None,"GEOMETRYFIELDb":None,\
                           "GEOMETRYFIELD":"the_geom","KEYFIELD":"ogc_fid","BUFFERRADIUS":"","FIELD":"","SIMPLEFIELD":"","FIELDb":"","JOIN":"",\
                           "ORDERBY":"","WHERE":"","OPERATOR":"","CONDITION":"","SPATIALREL":None,"SPATIALFROM":"",\
                           "SPATIALRELNOT":" ","FIDFIELD":"","FIELDSET":"","GROUPBYSET":"", "ONLYGEOMSET":"", "MATERIALIZED":"","DISTANCEOP":"","DISTANCE":"","SCHEMA":""}
        self.currentQuery = ""
        self.fieldSet = []
    
    def getSpatialRelationships(self):
        return self.spatialRel.keys()

    def resetQueryParametersCheckList(self):
        self.QueryParametersCheckList = {}
        for p in self.getRequiredParameters():
            self.QueryParametersCheckList[p] = None
        #print "resetQueryParametersCheckList"
        return dict

    def setQueryParametersCheckList(self,key):
        self.QueryParametersCheckList[key]=True
    
    def testQueryParametersCheckList(self):
        if self.currentQuery == "":
            return None
        res = True
        for key,value in self.QueryParametersCheckList.iteritems():
            #print key,value
            res = res and value
        #print res
        return res

    def getParameter(self,par):
        return self.parameters[par]

    def getQueryLabels(self):
        return self.querySet.keys()
    
    def getDescription(self):
        return self.querySet[self.currentQuery][0]
        
    def getHelp(self):
        return self.querySet[self.currentQuery][1]

    def getRequiredSlots(self):
        return self.querySet[self.currentQuery][2]

    def getRequiredParameters(self):
        req = self.querySet[self.currentQuery][2]
        #print req
        cleanReq=[]
        for elem in req:
            if not((elem == 'fieldsListA') or (elem == 'fieldsListB')):
                cleanReq.append(elem)
        return cleanReq
        
    def setCurrentQuery(self,q):
        self.currentQuery = q
        #print q
        self.resetQueryParametersCheckList()
        
    def getQueryTemplate(self):
        return self.querySet[self.currentQuery][3]
    
    def setParameter(self,var,value):
        #print "set "+var+": ",value
        if var in self.parameters:
            self.parameters[var] = value
            try:
                self.QueryParametersCheckList[var]=True
            except:
                pass
        else:
            #print "ALERT: variable not found"
            pass

    def buildFIELDSET(self):
        if not self.parameters["GEOMETRYFIELDa"]:
            self.parameters["GEOMETRYFIELDa"] = self.parameters["GEOMETRYFIELD"]
        if not self.parameters["GEOMETRYFIELDb"]:
            self.parameters["GEOMETRYFIELDb"] = self.parameters["GEOMETRYFIELD"]
        self.parameters["SCHEMA"] = self.schemaName
        self.parameters["FIELDSET"]=""
        self.parameters["GROUPBYSET"]=""
        self.parameters["ONLYGEOMSET"]=("row_number() OVER () AS %s" % (self.parameters["KEYFIELD"]))
        for e in self.fieldSet:
            self.parameters["FIELDSET"] += e+','
            if not (e.find(self.parameters["GEOMETRYFIELD"])!=-1):
                self.parameters["GROUPBYSET"] += e+','
        test = None
        for f in self.fieldSet:
            #print f[-len(self.parameters["KEYFIELD"])-1:-1]
            if (f[-len(self.parameters["KEYFIELD"])-1:-1] == self.parameters["KEYFIELD"]):
                test = True
        if self.fieldSet==[] or not test:
            self.parameters["FIELDSET"] += ('row_number() OVER () AS "%s"' % (self.parameters["KEYFIELD"]))
        else:
            self.parameters["FIELDSET"]=self.parameters["FIELDSET"][:len(self.parameters["FIELDSET"])-1]
        if self.parameters["GROUPBYSET"]!="":
            self.parameters["GROUPBYSET"]="GROUP BY "+self.parameters["GROUPBYSET"][:len(self.parameters["GROUPBYSET"])-1]
        #print "FIELDSET:",self.parameters["FIELDSET"]
        #print "GROUPBYSET:",self.parameters["GROUPBYSET"]


    def getQueryParsed(self,isView):
        if self.testIfQueryDefined():
            if isView:
                viewDef = 'CREATE %s VIEW "%s"."%s" AS ' % (self.parameters["MATERIALIZED"],self.parameters["SCHEMA"],self.parameters["VIEWNAME"])
            else:
                viewDef = ''
            self.buildFIELDSET()
            q = self.querySet[self.currentQuery][3]
            q = q.replace("[[","%(")
            q = q.replace("]]",")s")
            return format(viewDef + q % self.parameters,reindent=True)
            #print viewDef + q % self.parameters
        else:
            return ""

    def getNameParsed(self):
        if self.testIfQueryDefined():
            q = self.querySet[self.currentQuery][4]
            q = q.replace("[[","%(")
            q = q.replace("]]",")s")
            q = q % self.parameters
            q = q.replace("__","_")
            return q.strip()
        else:
            return ""

    def testIfQueryDefined(self):
        if self.currentQuery == "":
            return None
        test = True
        for requestedPar in self.getRequiredParameters():
            if self.parameters[requestedPar] == "":
                test = None
        return test

    def All(self):
        return self.querySet

    def formatSqlStatement(self,sql):
        return format(sql,reindent=True)