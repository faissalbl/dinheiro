from transforms.GenericTransform import GenericTransform
from models.Parameter import Parameter

class ParameterTransf(GenericTransform):
    
    def getModelType(self):
        return Parameter

    def buildJoinedModels(self, model, row):
        pass