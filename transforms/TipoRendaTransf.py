from transforms.GenericTransform import GenericTransform
from models.TipoRenda import TipoRenda

class TipoRendaTransf(GenericTransform):
    
    def getModelType(self):
        return TipoRenda

    def buildJoinedModels(self, model, row):
        pass