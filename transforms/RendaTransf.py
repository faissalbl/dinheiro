from transforms.GenericTransform import GenericTransform
from models.Renda import Renda
from models.Month import Month
from models.TipoRenda import TipoRenda

class RendaTransf(GenericTransform):
    
    def getModelType(self):
        return Renda

    def buildJoinedModels(self, model, row):
        keys = row.keys()
        model.tipoRenda = TipoRenda(
            id = row['tipo_renda_id'], 
            desc = row['desc'] if 'desc' in keys else None,
            auto = row['auto'] if 'auto' in keys else None)

        model.month = Month(
            id = row['month_id'] if 'month_id' in keys else None,
            month = row['month'] if 'month' in keys else None
        )
