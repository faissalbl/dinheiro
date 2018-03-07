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
        summary.rendas = RendaProcessor(month = self.month).ls()
        summary.despesasAnuais = DespesaAnualProcessor(month = self.month).ls()
        summary.despesasMensais = DespesaMensalProcessor(month = self.month).ls()
        summary.despesasTemp = DespesaTempProcessor(month = self.month).ls()
        return summary