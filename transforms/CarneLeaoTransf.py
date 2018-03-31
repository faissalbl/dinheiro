from transforms.GenericTransform import GenericTransform
from models.CarneLeao import CarneLeao
from models.Month import Month

class CarneLeaoTransf(GenericTransform):
    
    def getModelType(self):
        return CarneLeao

    def buildJoinedModels(self, model, row):
        model.month = Month(
            id = row['month_id'],
            month = row['month'],
            user = row['user'])