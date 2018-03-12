import sqlite3
import os
from operator import attrgetter

absPath = os.path.abspath(__file__)
dirname, filename = os.path.split(absPath)
db_path = dirname + '/../db/dinheiro-db.sqlite'

class GenericDAO:

    def find(self, model):
        query = self.getQuery(model, 'find')
        params = self.buildParams(model)
        result = self.executeQuery(query, params = params)
        return result

    #----------------------------------------------------------------------------------
    # adds a model. It will not fetch dependent models. All foreign ids must be filled
    # in.
    #----------------------------------------------------------------------------------
    def add(self, model):
        query = self.getQuery(model, 'add')
        params = self.buildParams(model, insert = True)
        return self.executeUpdate(query, params = params)

    def update(self, model):
        query = self.getQuery(model, 'update')
        params = self.buildParams(model)
        self.executeUpdate(query, params = params)

    def delete(self, model):
        query = self.getQuery(model, 'delete')
        params = self.buildParams(model)
        self.executeUpdate(query, params = params)

    def buildParams(self, model, insert = False):
        d = self.getPropertyToColumnDict(model)
        params = {}
        for prop, col in d.items():
            # id is ignored on insert, because it's autoincremented
            if (insert and (prop == 'id' or not self.isInModel(model, prop))):
                continue

            propVal = attrgetter(prop)(model)
            params[col] = propVal

        return params

    def isInModel(self, model, prop):
        result = True
        try:
            attrgetter(prop)(model)
        except AttributeError:
            result = False

        return result


    def getPropertyToColumnDict(self, model):
        d = model.getPropertyToColumnDict()
        if (not d):
            raise Exception('no property to column dict was found for the model {}'.format(model.__name__))

        return d

    def getQuery(self, model, queryName):
        queryModule = model.getQueryModule()
        queryDict = queryModule.queries
        if (not queryDict):
            raise Exception('Could not find \'queries\' dict in ' + queryModule.__name__)

        query = queryDict[queryName]

        if (not query):
        	raise Exception('Could not find \'{}\' query in {}'.format(queryName, queryModule.__name__))

        return query

    #----------------------------------------------------------------------------------
    # executeQuery: 
    # executes query and, if a transform is provided by the subclass via getTransform()
    # then the result (cols, rows) will be converted into a list of specific objects,
    # like TipoRenda
    #----------------------------------------------------------------------------------
    def executeQuery(self, query, params = None, fetchone = False):
        con, cur = self.connect()

        params = self.formatParams(params)
        cur.execute(query, params)
        
        rows = None
        if (fetchone):
            rows = cur.fetchone()
        else:
            rows = cur.fetchall()

        cols = []
        for coldesc in cur.description:
            cols.append(coldesc[0])

        result = (tuple(cols), rows)

        transform = self.getTransform()
        if (transform):
            result = transform.transform(result)                   

        return result 

    def executeUpdate(self, query, params = None):
        con, cur = self.connect()    
        params = self.formatParams(params)
        cur.execute(query, params)
        con.commit()
        return cur.lastrowid

    def formatParams(self, params):
        result = params
        if (not params):
            result = ()
        elif (type(params) == 'list'):
            result = tuple(params)

        return result


    def connect(self, params = None):
        con = sqlite3.connect(db_path)
        con.execute('pragma foreign_keys = ON;')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        return (con, cur)

    def getTransform(self):
    	raise NotImplementedError('not implemented')

