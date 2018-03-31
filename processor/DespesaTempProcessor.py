from datetime import date
from processor.DespesaChildProcessor import DespesaChildProcessor
from models.DespesaTemp import DespesaTemp
from models.Pagamento import Pagamento
from dao.DespesaTempDAO import DespesaTempDAO
from utils import DateUtil

class DespesaTempProcessor(DespesaChildProcessor):

    def __init__(self, month = None):
        super().__init__(month = month)
        self.despesaTempDAO = DespesaTempDAO()
    
    def getDAO(self):
        return self.despesaTempDAO

    def getModelType(self):
        return DespesaTemp

    def add(self, model):
        if model.months:
            pMonth = self.month.month
            for i in range(model.months):
                pagamento = Pagamento(val = model.despesa.val, month = pMonth)
                model.pagamentos.append(pagamento)
                pMonth = DateUtil.nextMonth(pMonth)

        super().add(model)

    def pay(self, model):
        model.despesa.month = self.month
        models = self.despesaTempDAO.find(model)

        if len(models) != 1:
            return

        model = models[0]

        countPaid = 0
        for p in model.pagamentos:
            if p.month == str(self.month.month):
                p.paid = 1

            if (p.paid):
                countPaid += 1

        if countPaid == len(model.pagamentos):
            model.despesa.paid = 1

        model.paidMonths = countPaid
        self.getDAO().update(model)

    def copy(self):
        pass