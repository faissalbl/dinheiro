from models.GenericModel import GenericModel
from collections import OrderedDict

class DespesaMensal(GenericModel):
    
    def __init__(self, despesa = None):
        self.despesa = despesa

    def __str__(self):
        return "DespesaMensal [despesa: {}]".format(self.despesa)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesa.id'] = 'despesa_id'
        d['despesa.month'] = 'month'
        return d     
