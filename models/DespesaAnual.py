from models.GenericModel import GenericModel
from models.Despesa import Despesa
from collections import OrderedDict

class DespesaAnual(Despesa):
    
    despesa = None
    savedVal = None

    def __init__(self, despesa = None, savedVal = None):
        self.despesa = despesa
        self.savedVal = savedVal

    def __str__(self):
        return "[despesa: {}, savedVal: {}]".format(self.despesa, self.savedVal)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesa.id'] = 'despesa_id'
        d['despesa.month'] = 'month'
        d['savedVal'] = 'saved_val'
        return d     

    def getParentModel(self):
        return self.despesa