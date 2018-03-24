from collections import OrderedDict
import importlib

class GenericModel:

    #------------------------------------------------------
    # Each model must know how to set the month it belongs to
    #------------------------------------------------------   
    def setMonth(self, month):
        raise NotImplementedError('This has to be implemented by the subclass')

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

    def defOutputStr(self):
        raise NotImplementedError('Implement defOutputStr')

    def defOutputStrHeader(self):
        raise NotImplementedError('Implement defOutputStrHeader')

    def defOutputHr(self):
        raise NotImplementedError('Implement defOutputHr')