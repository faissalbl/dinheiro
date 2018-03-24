from processor.RendaProcessor import RendaProcessor
from processor.DespesaAnualProcessor import DespesaAnualProcessor
from processor.DespesaMensalProcessor import DespesaMensalProcessor
from processor.DespesaTempProcessor import DespesaTempProcessor
from models.Summary import Summary

class SummaryProcessor:

    def __init__(self, month = None):
        self.month = month

    def buildSummary(self):
        summary = Summary()
        summary.rendas = RendaProcessor(month = self.month).find()
        summary.despesasAnuais = DespesaAnualProcessor(month = self.month).find()
        summary.despesasMensais = DespesaMensalProcessor(month = self.month).find()
        summary.despesasTemp = DespesaTempProcessor(month = self.month).find()
        return summary