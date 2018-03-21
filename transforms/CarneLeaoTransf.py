from transforms.GenericTransform import GenericTransform
from models.CarneLeao import CarneLeao

class CarneLeaoTransf(GenericTransform):
    
    def getModelType(self):
        return CarneLeao

    def buildJoinedModels(self, model, row):
        pass