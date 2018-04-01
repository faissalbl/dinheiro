from models.DespesaChild import DespesaChild
from collections import OrderedDict

class DespesaTemp(DespesaChild):
    
    def __init__(self, despesa = None, months = None, paidMonths = None):
        super().__init__(despesa)
        self.months = int(months) if months != None else None
        self.paidMonths = int(paidMonths) if paidMonths != None else None
        self.pagamentos = []

    def getPagamento(month):
        result = None
        for pagamento in self.pagamentos:
            if pagamento.month == month:
                result = pagamento
                break
        return result

    def __str__(self):
        return "DespesaTemp [despesa: {}, months: {}, paidMonths: {}]".format(
            self.despesa, self.months, self.paidMonths)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d.update(super().getPropertyToColumnDict())
        d['months'] = 'months'
        d['paidMonths'] = 'paid_months'
        return d     

    def defOutputStr(self):
        result = super().defOutputStr()
        result += str(self.months if self.months != None else '').rjust(6, ' ').ljust(8, ' ')
        result += str(self.paidMonths if self.paidMonths != None else '').rjust(11, ' ').ljust(13, ' ')

        return result
        
    def defOutputStrHeader(self):
        result = super().defOutputStrHeader()
        result += 'MONTHS'.rjust(6, ' ').ljust(8, ' ')
        result += 'PAID MONTHS'.rjust(11, ' ').ljust(13, ' ')
        return result
