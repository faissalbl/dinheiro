from transforms.DespesaChildTransf import DespesaChildTransf
from models.DespesaTemp import DespesaTemp

class DespesaTempTransf(DespesaChildTransf):
    
    def getModelType(self):
        return DespesaTemp