from processor.DespesaChildProcessor import DespesaChildProcessor
from models.DespesaTemp import DespesaTemp
from dao.DespesaTempDAO import DespesaTempDAO

class DespesaTempProcessor(DespesaChildProcessor):

    def __init__(self):
        super().__init__()
        self.despesaTempDAO = DespesaTempDAO()
    
    def getDAO(self):
        return self.despesaTempDAO

    def getModelType(self):
        return DespesaTemp
