from processor.GenericProcessor import GenericProcessor
from models.Renda import Renda
from models.TipoRenda import TipoRenda
from dao.TipoRendaDAO import TipoRendaDAO
from dao.RendaDAO import RendaDAO

class RendaProcessor(GenericProcessor):

    def __init__(self, month = None):
        super().__init__(month = month)
        self.rendaDAO = RendaDAO()
    
    def getDAO(self):
        return self.rendaDAO

    def getModelType(self):
        return Renda

    def calculateReserva(self):
        # sum despesa anual divided by 12.0 (float) months
        from processor.DespesaAnualProcessor import DespesaAnualProcessor
        from processor.DespesaMensalProcessor import DespesaMensalProcessor
        from processor.DespesaTempProcessor import DespesaTempProcessor
        sumDespesaAnual = DespesaAnualProcessor(month = self.month).sum() / 12.0
        sumDespesaMensal = DespesaMensalProcessor(month = self.month).sum()
        sumDespesaTemp = DespesaTempProcessor(month = self.month).sum()

        return sumDespesaAnual + sumDespesaMensal + sumDespesaTemp

    def refreshReserva(self):
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

