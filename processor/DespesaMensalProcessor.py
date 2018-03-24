from processor.DespesaChildProcessor import DespesaChildProcessor
from models.DespesaMensal import DespesaMensal
from models.Despesa import Despesa
from dao.DespesaMensalDAO import DespesaMensalDAO

class DespesaMensalProcessor(DespesaChildProcessor):

    def __init__(self, month = None):
        super().__init__(month = month)
        self.despesaMensalDAO = DespesaMensalDAO()
        self.despesaMensalProcessor = DespesaMensalProcessor(month = month)

    def getDAO(self):
        return self.despesaMensalDAO

    def getModelType(self):
        return DespesaMensal

    def updateDespReservaAnual(self):
        despReservaAnual = DespesaMensal(Despesa(month = self.month, desc = 'Reserva Anual'), 
            auto = 1)
        despReservaAnual.despesa.val = self.calculateDespReservaAnual()
        
        despesasMensais = self.despesaMensalDAO.find(despReservaAnual)
        despesaMensal = None
        if len(depesasMensais) == 1:
            despesaMensal = despesasMensais[0]
            despesaMensal.despesa.val = despReservaAnual.val
        else:
            despesaMensal = despReservaAnual

        if despesaMensal.despesa.id:
            self.update(despesaMensal)
        else:
            self.add(despesaMensal)

    def calculateDespReservaAnual(self):
        # sum despesa anual divided by 12.0 (float) months
        from processor.DespesaAnualProcessor import DespesaAnualProcessor
        return DespesaAnualProcessor(month = self.month).sum() / 12.0


