from models.GenericModel import GenericModel
from models.Despesa import Despesa
from collections import OrderedDict

class DespesaChild(GenericModel):

    def __init__(self, despesa = None):
        self.despesa = despesa if despesa != None else Despesa()

    def setMonth(self, month):
        self.despesa.month = month

    def getMonth(self):
        return self.despesa.month        

    def defOutputStr(self):
        result = self.despesa.defOutputStr()
        return result
        
    def defOutputStrHeader(self):
        result = self.despesa.defOutputStrHeader()
        return result

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesa.id'] = 'despesa_id'
        d['despesa.desc'] = 'desc'
        d['despesa.month.id'] = 'month_id'
        d['despesa.month.month'] = 'month'
        d['despesa.month.user'] = 'user'
        return d     
