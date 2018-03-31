from transforms.GenericTransform import GenericTransform
from models.Despesa import Despesa
from models.Month import Month

class DespesaChildTransf(GenericTransform):
    
    def buildJoinedModels(self, model, row):
        keys = row.keys()
        model.despesa = Despesa(
            id = row['id'] if 'id' in keys else None, 
            desc = row['desc'] if 'desc' in keys else None, 
            val = row['val'] if 'val' in keys else None, 
            paidVal = row['paid_val'] if 'paid_val' in keys else None, 
            paid = row['paid'] if 'paid' in keys else None, 
            month = Month(
                id = row['month_id'] if 'month_id' in keys else None,
                month = row['month'] if 'month' in keys else None
            )
        )