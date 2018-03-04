from datetime import date
from processor.DespesaChildProcessor import DespesaChildProcessor
from models.DespesaTemp import DespesaTemp
from models.Pagamento import Pagamento
from dao.DespesaTempDAO import DespesaTempDAO

class DespesaTempProcessor(DespesaChildProcessor):

    def __init__(self):
        super().__init__()
        self.despesaTempDAO = DespesaTempDAO()
    
    def getDAO(self):
        return self.despesaTempDAO

    def getModelType(self):
        return DespesaTemp

    def add(self, model):
        if model.months:
            initialMonth = self.month
            for i in range(model.months):
                month = date(self.month.year, self.month.month + i, self.month.day)
                pagamento = Pagamento(val = model.despesa.val, month = month)
                model.pagamentos.append(pagamento)

        super().add(model)

    def pay(self, model):
        model.despesa.month = self.month
        models = self.despesaTempDAO.find(model)

        if len(models) != 1:
            return

        model = models[0]

        countPaid = 0
        for p in model.pagamentos:
            if p.month == str(self.month):
                p.paid = 1

            if (p.paid):
                countPaid += 1

        if countPaid == len(model.pagamentos):
            model.despesa.paid = 1

        model.paidMonths = countPaid
        self.getDAO().update(model)