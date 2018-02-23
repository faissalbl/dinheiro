from transforms.GenericTransform import GenericTransform
from models.Despesa import Despesa
from models.DespesaAnual import DespesaAnual

class DespesaAnualTransf(GenericTransform):
    
    def getModelType(self):
        return DespesaAnual

    def buildJoinedModels(self, model, row):
        model.despesa = Despesa(
            id = row['id'], 
            desc = row['desc'], 
            val = row['val'], 
            paidVal = row['paid_val'], 
            paid = row['paid'], 
            month = row['month'])