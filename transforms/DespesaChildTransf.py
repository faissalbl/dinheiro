from transforms.GenericTransform import GenericTransform
from models.Despesa import Despesa

class DespesaChildTransf(GenericTransform):
    
    def buildJoinedModels(self, model, row):
        model.despesa = Despesa(
            id = row['id'], 
            desc = row['desc'], 
            val = row['val'], 
            paidVal = row['paid_val'], 
            paid = row['paid'], 
            month = row['month'])