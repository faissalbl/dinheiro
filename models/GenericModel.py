from collections import OrderedDict
import importlib

class GenericModel:

    #------------------------------------------------------
    # Builds a dictionary that translates model properties'
    # names to table column names.
    # THIS MUST RETURN a collections.OrderedDict
    #------------------------------------------------------
    def getPropertyToColumnDict(self):
        raise NotImplementedError('This has to be implemented by the subclass')

    #------------------------------------------------------
    # Builds a dictionary that translates table column names
    # to model properties' names.
    # THIS MUST RETURN a collections.OrderedDict
    #------------------------------------------------------
    def getColumnToPropertyDict(self):
        d = OrderedDict()
        for k, v in self.getPropertyToColumnDict().items():
            d[v] = k
        return d
    
    #------------------------------------------------------------------------
    # Loads the model specific queries model: example: DespesaQueries
    #------------------------------------------------------------------------    
    def getQueryModule(self):
        modName = type(self).__name__ + 'Queries'
        modName = 'models.queries.' + modName
        queryModule = importlib.import_module(modName)
        return queryModule