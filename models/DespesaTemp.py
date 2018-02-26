from models.GenericModel import GenericModel
from collections import OrderedDict

class DespesaTemp(GenericModel):
    
    despesa = None
    months = None
    paidMonths = None
    pagamentos = []

    def __init__(self, despesa = None, months = None, paidMonths = None):
        self.despesa = despesa
        self.months = months
        self.paidMonths = paidMonths

    def getPagamentoMonth(self):
        result = None
        if self.despesa and self.despesa.month:
            for pagamento in pagamentos:
                if pagamento.month == self.despesa.month:
                    result = pagamento
        return result

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