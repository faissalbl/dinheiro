import os
from dao.GenericDAO import GenericDAO
from transforms.CarneLeaoTransf import CarneLeaoTransf

class CarneLeaoDAO(GenericDAO):

    def getTransform(self):
        return CarneLeaoTransf()
