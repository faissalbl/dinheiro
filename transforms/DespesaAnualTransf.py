from transforms.DespesaChildTransf import DespesaChildTransf
from models.DespesaAnual import DespesaAnual

class DespesaAnualTransf(DespesaChildTransf):
    
    def getModelType(self):
        return DespesaAnual
