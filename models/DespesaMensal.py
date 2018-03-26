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

    def defOutputStr(self):
        result = super().defOutputStr()
        result += str(self.auto).rjust(4, ' ').ljust(6, ' ')
        return result
        
    def defOutputStrHeader(self):
        result = super().defOutputStrHeader()
        result += 'AUTO'.rjust(4, ' ').ljust(6, ' ')
        return result
