from models.GenericModel import GenericModel
from models.Despesa import Despesa
from collections import OrderedDict

class DespesaTemp(Despesa):
    
    despesa = None
    months = None
    paidMonths = None

    def __init__(self, despesa = None, months = None, paidMonths = None):
        self.despesa = despesa
        self.months = months
        self.paiMonths = paidMonths

    def __str__(self):
        return "[despesa: {}, months: {}, paidMonths: {}]".format(
            self.despesa, self.months, self.paidMonths)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesa.id'] = 'despesa_id'
        d['despesa.month'] = 'month'
        d['months'] = 'months'
        d['paidMonths'] = 'paid_months'
        return d     

    def getParentModel(self):
        return self.despesa