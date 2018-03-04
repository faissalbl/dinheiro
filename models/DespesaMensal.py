from models.DespesaChild import DespesaChild
from collections import OrderedDict

class DespesaMensal(DespesaChild):
    
    def __str__(self):
        return "DespesaMensal [despesa: {}]".format(self.despesa)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesa.id'] = 'despesa_id'
        d['despesa.month'] = 'month'
        return d     
