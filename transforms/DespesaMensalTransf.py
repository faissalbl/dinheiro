from transforms.DespesaChildTransf import DespesaChildTransf
from models.DespesaMensal import DespesaMensal

class DespesaMensalTransf(DespesaChildTransf):
    
    def getModelType(self):
        return DespesaMensal
