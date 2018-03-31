from transforms.GenericTransform import GenericTransform
from models.Month import Month

class MonthTransf(GenericTransform):
    
    def getModelType(self):
        return Month

    def buildJoinedModels(self, model, row):
        pass