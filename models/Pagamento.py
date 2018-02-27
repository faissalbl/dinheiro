from models.GenericModel import GenericModel
from models.DespesaTemp import DespesaTemp
from collections import OrderedDict

class Pagamento(GenericModel):
    
    def __init__(self, despesaTemp = None, val = None, paid = None, month = None):
        self.despesaTemp = despesaTemp
        self.val = val
        self.paid = paid
        self.month = month

    def __str__(self):
        return "[despesaTemp: {}, val: {}, paid: {}, month: {}]".format(
            self.despesaTemp, self.val, self.paid, self.month)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesaTemp.despesa.id'] = 'despesa_id'
        d['despesaTemp.despesa.month'] = 'despesa_month'
        d['val'] = 'val'
        d['paid'] = 'paid'
        d['month'] = 'month'
        return d     
