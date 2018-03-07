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
        d['despesa.id'] = 'despesa_id'
        d['despesa.month'] = 'month'
        d['months'] = 'months'
        d['paidMonths'] = 'paid_months'
        return d     
