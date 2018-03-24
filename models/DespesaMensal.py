from models.DespesaChild import DespesaChild
from collections import OrderedDict

class DespesaMensal(DespesaChild):

    def __init__(self, despesa = None, auto = None):
        super().__init__(despesa = despesa)
        self.auto = auto
    
    def __str__(self):
        return "DespesaMensal [despesa: {}, auto: {}]".format(self.despesa, self.auto)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesa.id'] = 'despesa_id'
        d['despesa.month'] = 'month'
        d['despesa.desc'] = 'desc'
        d['auto'] = 'auto'
        return d     
