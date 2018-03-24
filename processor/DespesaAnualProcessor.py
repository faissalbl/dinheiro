from processor.GenericProcessor import GenericProcessor
from processor.DespesaChildProcessor import DespesaChildProcessor
from processor.DespesaMensalProcessor import DespesaMensalProcessor
from models.DespesaAnual import DespesaAnual
from dao.DespesaAnualDAO import DespesaAnualDAO

class DespesaAnualProcessor(DespesaChildProcessor):

    def __init__(self, month = None):
        super().__init__(month = month)
        self.despesaAnualDAO = DespesaAnualDAO()
        self.despesaMensalProcessor = DespesaMensalProcessor(month = month)
    
    def getDAO(self):
        return self.despesaAnualDAO

    def getModelType(self):
        return DespesaAnual

    def add(self, model):
        # skipping DespesaChildProcessor intentionally to avoid post CRUD actions
        GenericProcessor.add(self, model)
        self.despesaMensalProcessor.updateDespReservaAnual()

    def delete(self, model):
        # skipping DespesaChildProcessor intentionally to avoid post CRUD actions
        GenericProcessor.delete(self, model)
        self.despesaMensalProcessor.updateDespReservaAnual()

    def update(self, model):
        # skipping DespesaChildProcessor intentionally to avoid post CRUD actions
        GenericProcessor.update(self, model)
        self.despesaMensalProcessor.updateDespReservaAnual()
