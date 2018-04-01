from processor.GenericProcessor import GenericProcessor
from dao.ParameterDAO import ParameterDAO
from models.Parameter import Parameter

class ParameterProcessor(GenericProcessor):

    def __init__(self):
        super().__init__(None)
        self.parameterDAO = ParameterDAO()
    
    def getDAO(self):
        return self.parameterDAO

    def getModelType(self):
        return Parameter

    def getCarneLeaoPercIncome(self):
        parameterFilter = Parameter(namespace = 'carne_leao', name = 'perc')
        paramResult = ParameterDAO().find(parameterFilter)
        param = None
        if (len(paramResult) == 1):
            param = paramResult[0]

        return param.val if param else 1
    
    def getCarneLeaoActive(self):
        parameterFilter = Parameter(namespace = 'carne_leao', name = 'active')
        paramResult = ParameterDAO().find(parameterFilter)
        param = None
        if (len(paramResult) == 1):
            param = paramResult[0]

        return param.val if param else 0
