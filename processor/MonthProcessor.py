from processor.RendaProcessor import RendaProcessor
from processor.DespesaMensalProcessor import DespesaMensalProcessor

class MonthProcessor:

    def changeMonth(month):
        despesaMensalProcessor = DespesaMensalProcessor(month = month)

        despMensalCount = despesaMensalProcessor.count()

        if despMensalCount == 0:
            print('Copying despesas from the past months...')
            despesaMensalProcessor.copy()
            print('...Done')

        despesaMensalProcessor.updateDespCarneLeao()