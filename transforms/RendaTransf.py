from transforms.GenericTransform import GenericTransform
from models.Renda import Renda
from models.TipoRenda import TipoRenda

class RendaTransf(GenericTransform):
    
    def getModelType(self):
        return Renda

    def buildJoinedModels(self, model, row):
        model.tipoRenda = TipoRenda(id = row['tipo_renda_id'], desc = row['desc'])