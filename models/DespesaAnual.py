from models.DespesaChild import DespesaChild
from collections import OrderedDict

class DespesaAnual(DespesaChild):
    
    def __init__(self, despesa = None, savedVal = None):
        super().__init__(despesa)
        self.savedVal = float(savedVal) if savedVal != None else None

    def __str__(self):
        return "DespesaAnual [despesa: {}, savedVal: {}]".format(self.despesa, self.savedVal)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesa.id'] = 'despesa_id'
        d['despesa.month'] = 'month'
        d['savedVal'] = 'saved_val'
        return d     
