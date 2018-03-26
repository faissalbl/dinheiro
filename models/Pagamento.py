from models.GenericModel import GenericModel
from models.DespesaTemp import DespesaTemp
from collections import OrderedDict

class Pagamento(GenericModel):
    
    def __init__(self, despesaTemp = None, val = None, paid = None, month = None):
        self.despesaTemp = despesaTemp if despesaTemp != None else DespesaTemp()
        self.val = float(val) if val != None else None
        self.paid = int(paid) if paid != None else None
        self.month = month

    def __str__(self):
        return "Pagamento [despesa.id: {}, val: {}, paid: {}, month: {}]".format(
            self.despesaTemp.despesa.id, self.val, self.paid, self.month)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['despesaTemp.despesa.id'] = 'despesa_id'
        d['despesaTemp.despesa.month'] = 'despesa_month'
        d['val'] = 'val'
        d['paid'] = 'paid'
        d['month'] = 'month'
        return d     

    def defOutputStr(self):
        result = str(self.val).rjust(7, ' ').ljust(9, ' ')
        result += str(self.paid).rjust(4, ' ').ljust(6, ' ')
        result += str(self.month).ljust(12, ' ')
        return result
        
    def defOutputStrHeader(self):
        result = 'VAL'.rjust(7, ' ').ljust(9, ' ')
        result += 'PAID'.rjust(4, ' ').ljust(6, ' ')
        result += 'MONTH'.ljust(12, ' ')
        return result