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