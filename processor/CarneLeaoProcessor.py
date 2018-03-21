from processor.GenericProcessor import GenericProcessor
from dao.RendaDAO import RendaDAO
from models.Renda import Renda
from models.CarneLeao import CarneLeao
from dao.CarneLeaoDAO import CarneLeaoDAO

class CarneLeaoProcessor(GenericProcessor):

    def __init__(self):
        super().__init__()
        self.carneLeaoDAO = CarneLeaoDAO()
    
    def getDAO(self):
        return self.carneLeaoDAO

    def getModelType(self):
        return CarneLeao

    def calculateCarneLeao(self):
        rendaDAO = RendaDAO()
        rendaFilter = Renda(month = self.month, taxable = 1)
        rendas = rendaDAO.find(rendaFilter)

        # TODO implement parametro dao to get the percent of income to declare
        # (carne_leao   perc)

        # need to parameterize this if carne leao withheld amount varies
        withheldPerc = 0.1
