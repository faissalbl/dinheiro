from processor.DespesaChildProcessor import DespesaChildProcessor
from models.DespesaAnual import DespesaAnual
from dao.DespesaAnualDAO import DespesaAnualDAO

class DespesaAnualProcessor(DespesaChildProcessor):

    def __init__(self, mon = None):
        super().__init__(mon = mon)
        self.despesaAnualDAO = DespesaAnualDAO()
    
    def getDAO(self):
        return self.despesaAnualDAO

    def getModelType(self):
        return DespesaAnual
