from processor.DespesaChildProcessor import DespesaChildProcessor
from processor.MonthProcessor import MonthProcessor
from processor.ParameterProcessor import ParameterProcessor
from models.DespesaMensal import DespesaMensal
from models.Despesa import Despesa
from models.CarneLeao import CarneLeao
from models.Month import Month
from dao.DespesaMensalDAO import DespesaMensalDAO
from dao.CarneLeaoDAO import CarneLeaoDAO
from utils import DateUtil

class DespesaMensalProcessor(DespesaChildProcessor):

    def __init__(self, month = None):
        super().__init__(month = month)
        self.despesaMensalDAO = DespesaMensalDAO()

    def getDAO(self):
        return self.despesaMensalDAO

    def getModelType(self):
        return DespesaMensal

    def updateDespReservaAnual(self):
        despReservaAnual = DespesaMensal(
            Despesa(month = self.month, desc = 'Reserva Anual'), 
            auto = 1)
        despReservaAnual.despesa.val = self.calculateDespReservaAnual()
        
        despesasMensais = self.despesaMensalDAO.find(despReservaAnual)
        despesaMensal = None
        if len(despesasMensais) == 1:
            despesaMensal = despesasMensais[0]
            despesaMensal.despesa.val = despReservaAnual.despesa.val
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

    def updateDespCarneLeao(self):
        carneLeaoActive = ParameterProcessor().getCarneLeaoActive()
        if carneLeaoActive:
            from processor.MonthProcessor import MonthProcessor
            
            previousMonth = DateUtil.previousMonth(self.month.month)
            previousMonthFilter = Month(month = previousMonth, user = self.month.user)
            previousMonth = None
            result = MonthProcessor(month = previousMonthFilter).find()
            if len(result) == 1:
                previousMonth = result[0]

            carneLeaoTax = 0.0
            if (previousMonth):
                carneLeao = CarneLeao(month = previousMonth)
                result = CarneLeaoDAO().find(carneLeao)
                carneLeao = None
                if len(result) == 1:
                    carneLeao = result[0]

                if carneLeao:
                   carneLeaoTax = carneLeao.tax

            despCarneLeao = DespesaMensal(
                Despesa(month = self.month, desc = 'Carne Leao {}'.format(previousMonthFilter.month), 
                val = carneLeaoTax),
                auto = 1)

            despesasMensais = self.despesaMensalDAO.find(despCarneLeao)
            despesaMensal = None
            if len(despesasMensais) == 1:
                despesaMensal = despesasMensais[0]
                despesaMensal.despesa.val = carneLeaoTax
            else:
                despesaMensal = despCarneLeao

            if despesaMensal.despesa.id:
                self.update(despesaMensal)
            else:
                self.add(despesaMensal)

