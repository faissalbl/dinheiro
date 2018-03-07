from processor.DespesaChildProcessor import DespesaChildProcessor
from models.DespesaMensal import DespesaMensal
from dao.DespesaMensalDAO import DespesaMensalDAO

class DespesaMensalProcessor(DespesaChildProcessor):

    def __init__(self, month = None):
        super().__init__(month = month)
        self.despesaMensalDAO = DespesaMensalDAO()

    def copyDespesasToMonth(self, model, month):
        self.despesaMensalDAO.copyDespesasToMonth(model, month)

    def getDAO(self):
        return self.despesaMensalDAO

    def getModelType(self):
        return DespesaMensal
