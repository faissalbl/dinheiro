from models.GenericModel import GenericModel
from models.DespesaTemp import DespesaTemp
from collections import OrderedDict

class DespesaTemp(Despesa):
    
    despesaTemp = None
    val = None
    paid = None
    month = None

    def __init__(self, despesaTemp = None, val = None, paid = None, month = None):
        self.despesaTemp = despesaTemp
        self.val = val
        self.paid = paid
        self.month = month

    def __str__(self):
        return "[despesa: {}, val: {}, paid: {}, month: {}]".format(
            self.despesa, self.val, self.paid, self.month

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesa.id'] = 'despesa_id'
        d['val'] = 'val'
        d['paid'] = 'paid'
        d['month'] = 'month'
        return d     
