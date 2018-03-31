from processor.GenericProcessor import GenericProcessor
from models.TipoRenda import TipoRenda
from dao.TipoRendaDAO import TipoRendaDAO

class TipoRendaProcessor(GenericProcessor):

    def __init__(self):
        super().__init__(None)
        self.tipoRendaDAO = TipoRendaDAO()
    
    def getDAO(self):
        return self.tipoRendaDAO

    def getModelType(self):
        return TipoRenda
