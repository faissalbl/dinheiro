from transforms.DespesaChildTransf import DespesaChildTransf
from models.Despesa import Despesa
from models.DespesaTemp import DespesaTemp

class DespesaTempTransf(DespesaChildTransf):
    
    def getModelType(self):
        return DespesaTemp