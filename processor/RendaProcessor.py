from processor.GenericProcessor import GenericProcessor
from processor.CarneLeaoProcessor import CarneLeaoProcessor
from models.Renda import Renda
from models.TipoRenda import TipoRenda
from dao.TipoRendaDAO import TipoRendaDAO
from dao.RendaDAO import RendaDAO

class RendaProcessor(GenericProcessor):

    def __init__(self, month = None):
        super().__init__(month = month)
        self.rendaDAO = RendaDAO()
        self.carneLeaoProcessor = CarneLeaoProcessor(month = month)
    
    def getDAO(self):
        return self.rendaDAO

    def getModelType(self):
        return Renda

    def add(self, model):
        super().add(model)
        self.carneLeaoProcessor.updateCarneLeao()

    def delete(self, model):
        super().delete(model)
        self.carneLeaoProcessor.updateCarneLeao()

    def update(self, model):
        super().update(model)
        self.carneLeaoProcessor.updateCarneLeao()

    def calculateReserva(self):
        from processor.DespesaMensalProcessor import DespesaMensalProcessor
        from processor.DespesaTempProcessor import DespesaTempProcessor
        sumDespesaMensal = DespesaMensalProcessor(month = self.month).sum()
        sumDespesaTemp = DespesaTempProcessor(month = self.month).sum()

        return sumDespesaMensal + sumDespesaTemp

    def updateReserva(self):
        rendaDAO = RendaDAO()
        tipoRenda = TipoRenda(auto = 1)
        tipoRenda = TipoRendaDAO().find(tipoRenda)[0]
        renda = Renda(month = self.month, tipoRenda = tipoRenda)
        result = rendaDAO.find(renda)

        update = False
        if len(result) > 0:
            renda = result[0]
            update = True
                    
        renda.val = self.calculateReserva()
        if update:
            self.rendaDAO.update(renda)
        else:
            self.rendaDAO.add(renda)

