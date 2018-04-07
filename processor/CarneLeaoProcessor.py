from processor.GenericProcessor import GenericProcessor
from processor.ParameterProcessor import ParameterProcessor
from dao.RendaDAO import RendaDAO
from models.Renda import Renda
from models.CarneLeao import CarneLeao
from dao.CarneLeaoDAO import CarneLeaoDAO

class CarneLeaoProcessor(GenericProcessor):

    def __init__(self, month = None):
        super().__init__(month = month)
        self.carneLeaoDAO = CarneLeaoDAO()
    
    def getDAO(self):
        return self.carneLeaoDAO

    def getModelType(self):
        return CarneLeao

    def updateCarneLeao(self):
        carneLeaoActive = ParameterProcessor().getCarneLeaoActive()
        if carneLeaoActive:
            carneLeao = self.calculateCarneLeao()
            # add: inserts or replaces a record
            self.carneLeaoDAO.add(carneLeao)

    def calculateCarneLeao(self):
        rendaDAO = RendaDAO()
        rendaFilter = Renda(month = self.month, taxable = 1)
        rendas = rendaDAO.find(rendaFilter)

        # percent of income to declare
        percIncome = ParameterProcessor().getCarneLeaoPercIncome()

       # need to parameterize this if carne leao withheld amount varies
        withheldPerc = 0.1

        totalRenda = 0.0
        for renda in rendas:
            totalRenda += renda.val

        taxableAmount = totalRenda * float(percIncome)
        withheldAmount = taxableAmount * withheldPerc

        return CarneLeao(month = self.month, income = taxableAmount, tax = withheldAmount)

