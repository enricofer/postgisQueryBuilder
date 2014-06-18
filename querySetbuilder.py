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
            'SELECT [[FIELDSET]],ST_Centroid("[[LAYERa]]".[[GEOMETRYFIELD]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]"',\
            '_Centroids_of_[[LAYERa]]'\
            ],\
            'ST_PointOnSurface':\
            [\
            'Returns a POINT guaranteed to lie on the surface of geomA.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_PointOnSurface.html',\
            ['LAYERa','fieldsListA'],\
            'SELECT [[FIELDSET]],ST_PointOnSurface("[[LAYERa]]".[[GEOMETRYFIELD]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]"',\
            '_Points_on_Surfaces_of_[[LAYERa]]'\
            ],\
            'ST_Union2 2 layer':\
            [\
            'Returns a geometry that represents the point set union of geomA and geomB.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Union.html',\
            ['LAYERa','LAYERb','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]],ST_Union("[[LAYERa]]".[[GEOMETRYFIELD]],"[[LAYERb]]".[[GEOMETRYFIELD]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]","[[SCHEMA]]"."[[LAYERb]]"',\
            '_Union_of_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'ST_Union 1 layer':\
            [\
            'Returns a geometry that represents the point set union of the Geometries in geomA.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Union.html',\
            ['LAYERa','fieldsListA'],\
            'SELECT [[FIELDSET]],ST_Union("[[LAYERa]]".[[GEOMETRYFIELD]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]"',\
            '_Union_of_[[LAYERa]]'\
            ],\
            'ST_Difference':\
            [\
            'Returns a geometry that represents that part of geometry A that does not intersect with geometry B.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Difference.html',\
            ['LAYERa','LAYERb','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]],ST_Difference("[[LAYERa]]".[[GEOMETRYFIELD]],"[[LAYERb]]".[[GEOMETRYFIELD]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]","[[SCHEMA]]"."[[LAYERb]]"',\
            '_Diff_between_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'ST_Intersection':\
            [\
            'Returns a geometry that represents the shared portion of geomA and geomB. The geography implementation does a transform to geometry to do the intersection and then transform back to WGS84.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Intersection.html',\
            ['LAYERa','LAYERb','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]],ST_Intersection("[[LAYERa]]".[[GEOMETRYFIELD]],"[[LAYERb]]".[[GEOMETRYFIELD]]) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]","[[SCHEMA]]"."[[LAYERb]]"',\
            '_Int_between_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'ST_Buffer':\
            [\
            'For geometry: Returns a geometry that represents all points whose distance from this Geometry is less than or equal to distance. Calculations are in the Spatial Reference System of this Geometry. For geography: Uses a planar transform wrapper.',\
            'http://postgis.refractions.net/documentation/manual-svn/ST_Buffer.html',\
            ['LAYERa','BUFFERRADIUS','fieldsListA'],\
            'SELECT [[FIELDSET]],ST_Buffer("[[LAYERa]]".[[GEOMETRYFIELD]],[[BUFFERRADIUS]]::double precision) AS [[GEOMETRYFIELD]] FROM "[[SCHEMA]]"."[[LAYERa]]"',\
            '_Buffer_of_[[LAYERa]]'\
            ],\
            'ADD MEASUREMENTS':\
            [\
            'Add area and perimeter measurements fields about LayerA geometries. For "geometry" type area is in SRID units. For "geography" area is in square meters.',\
            'http://postgis.org/docs/ST_Area.html',\
            ['LAYERa','fieldsListA'],\
            'SELECT [[FIELDSET]], ST_Area("[[LAYERa]]".[[GEOMETRYFIELD]]) AS Area_geom, ST_Perimeter("[[LAYERa]]".[[GEOMETRYFIELD]]) AS Perimeter_geom FROM "[[SCHEMA]]"."[[LAYERa]]"',\
            '_Measurements_of_[[LAYERa]]'\
            ],\
            'ADD DISTANCE FIELDS':\
            [\
            'Add maximum and minimum measure information between geometries of LayerA and LayerB. For geometry type Returns the 2-dimensional cartesian minimum and maximum distance (based on spatial ref) between two geometries in projected units. For geography type defaults to return spheroidal minimum distance between two geographies in meters." area is in square meters.',\
            'http://postgis.org/docs/ST_Distance.html',\
            ['LAYERa','LAYERb','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]], ST_Distance("[[LAYERa]]".[[GEOMETRYFIELD]],"[[LAYERb]]".[[GEOMETRYFIELD]]) AS MinDistance, ST_MaxDistance("[[LAYERa]]".[[GEOMETRYFIELD]],"[[LAYERb]]".[[GEOMETRYFIELD]]) AS MaxDistance FROM "[[SCHEMA]]"."[[LAYERa]]","[[SCHEMA]]"."[[LAYERb]]"',\
            '_Distances_between_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'SELECT BY ATTRIBUTE':\
            [\
            'Returns geometries whom attributes match query',\
            'http://www.postgresql.org/docs/8.2/static/sql-select.html',\
            ['LAYERa','FIELD','OPERATOR','CONDITION','fieldsListA'],\
            'SELECT [[FIELDSET]] FROM "[[SCHEMA]]"."[[LAYERa]]" WHERE [[FIELD]][[OPERATOR]][[CONDITION]]',\
            '_[[FIELD]]_Selection_of_[[LAYERa]]'\
            ],\
            'SELECT BY GEOMETRY':\
            [\
            'Returns features of geometry A that meet spatial condition respect geometry B',\
            'http://postgis.refractions.net/documentation/manual-svn/reference.html#Spatial_Relationships_Measurements',\
            ['LAYERa','LAYERb','SPATIALREL','SPATIALRELNOT','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]] FROM "[[SCHEMA]]"."[[LAYERa]]","[[SCHEMA]]"."[[LAYERb]]" WHERE [[SPATIALRELNOT]][[SPATIALREL]]("[[LAYERa]]".[[GEOMETRYFIELD]],"[[LAYERb]]".[[GEOMETRYFIELD]])',\
            '_Spatial_Relationship_between_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'SELECT BY DISTANCE':\
            [\
            'Returns features of geometry A that meet condition about distance respect geometry B',\
            'http://www.postgis.org/docs/ST_Distance.html',\
            ['LAYERa','LAYERb','DISTANCEOP','DISTANCE','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]] FROM "[[SCHEMA]]"."[[LAYERa]]","[[SCHEMA]]"."[[LAYERb]]" WHERE ST_Distance("[[LAYERa]]".[[GEOMETRYFIELD]],"[[LAYERb]]".[[GEOMETRYFIELD]]) [[DISTANCEOP]] [[DISTANCE]]',\
            '_Distance_selection_between_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'JOIN analytical':\
            [\
            'Returns the result of analytical join of Layer A and Layer B where field A meet field B',\
            'http://www.tutorialspoint.com/postgresql/postgresql_using_joins.htm',\
            ['LAYERa','LAYERb','FIELD','FIELDb','JOIN','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]] FROM "[[SCHEMA]]"."[[LAYERa]]" [[JOIN]] "[[SCHEMA]]"."[[LAYERb]]" ON "[[LAYERa]]".[[FIELD]] = "[[LAYERb]]".[[FIELDb]]',\
            '_analytical_join_of_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            'JOIN spatial':\
            [\
            'Returns the result of spatial join of Layer A and Layer B where relationship is true',\
            'http://workshops.boundlessgeo.com/postgis-intro/joins_exercises.html',\
            ['LAYERa','LAYERb','SPATIALREL','fieldsListA','fieldsListB'],\
            'SELECT [[FIELDSET]] FROM "[[SCHEMA]]"."[[LAYERa]]" INNER JOIN "[[SCHEMA]]"."[[LAYERb]]" ON [[SPATIALREL]]("[[LAYERa]]".[[GEOMETRYFIELD]],"[[LAYERb]]".[[GEOMETRYFIELD]])',\
            '_spatial_join_of_[[LAYERa]]_and_[[LAYERb]]'\
            ],\
            }

    def setSchema(self,schema):
        self.schemaName = schema

    def setIsView(self,bool):
        self.isView=bool

    def setFIDFIELD(self):
        self.parameters["FIDFIELD"]= "row_number() OVER () AS ogc_fid,"
    
    def unsetFIDFIELD(self):
        self.parameters["FIDFIELD"]= ""
    
    def setFieldsSet(self,list):
        self.fieldSet = list
    
    def resetParameters(self):
        self.parameters = {"VIEWNAME":"","LAYERa":"","LAYERb":"",\
                           "GEOMETRYFIELD":"the_geom","KEYFIELD":"ogc_fid","BUFFERRADIUS":"","FIELD":"","FIELDb":"","JOIN":"",\
                           "OPERATOR":"","CONDITION":"","SPATIALREL":None,\
                           "SPATIALRELNOT":" ","FIDFIELD":"","FIELDSET":"", "MATERIALIZED":"","DISTANCEOP":"","DISTANCE":"","SCHEMA":""}
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
        if var in self.parameters:
            self.parameters[var] = value
            self.QueryParametersCheckList[var]=True
        else:
            print "ALERT: variable not found"

    def buildFIELDSET(self):
        self.parameters["SCHEMA"] = self.schemaName
        self.parameters["FIELDSET"]=""
        for e in self.fieldSet:
            self.parameters["FIELDSET"] += e+','
        #print self.parameters["FIELDSET"]
        test = None
        for f in self.fieldSet:
            if (f[-len(self.parameters["KEYFIELD"]):] == self.parameters["KEYFIELD"]):
                test = True
        if self.fieldSet==[] or not test:
            self.parameters["FIELDSET"] += ("row_number() OVER () AS %s" % (self.parameters["KEYFIELD"]))
        else:
            self.parameters["FIELDSET"]=self.parameters["FIELDSET"][:len(self.parameters["FIELDSET"])-1]
        #print self.parameters["FIELDSET"]


    def getQueryParsed(self,isView):
        if self.testIfQueryDefined():
            if isView:
                viewDef = 'CREATE %s VIEW "%s" AS ' % (self.parameters["MATERIALIZED"],self.parameters["VIEWNAME"])
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
            return q
        else:
            return ""

    def testIfQueryDefined(self):
        test = True
        for requestedPar in self.getRequiredParameters():
            if self.parameters[requestedPar] == "":
                test = None
        return test

    def All(self):
        return self.querySet