from transforms.DespesaChildTransf import DespesaChildTransf
from models.Despesa import Despesa
from models.DespesaAnual import DespesaAnual

class DespesaAnualTransf(DespesaChildTransf):
    
    def getModelType(self):
        return DespesaAnual
