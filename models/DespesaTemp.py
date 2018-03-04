from models.DespesaChild import DespesaChild
from collections import OrderedDict

class DespesaTemp(DespesaChild):
    
    def __init__(self, despesa = None, months = None, paidMonths = None):
        super().__init__(despesa)
        self.months = int(months) if months != None else None
        self.paidMonths = int(paidMonths) if paidMonths != None else None
        self.pagamentos = []

    def getPagamentoMonth(self):
        result = None
        if self.despesa and self.despesa.month:
            for pagamento in pagamentos:
                if pagamento.month == self.despesa.month:
                    result = pagamento
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
