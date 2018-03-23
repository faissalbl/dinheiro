import os
from dao.GenericDAO import GenericDAO
from transforms.ParameterTransf import ParameterTransf

class ParameterDAO(GenericDAO):

    def getTransform(self):
        return ParameterTransf()
