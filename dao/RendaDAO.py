import os
from dao.GenericDAO import GenericDAO
from transforms.RendaTransf import RendaTransf

class RendaDAO(GenericDAO):

    def getTransform(self):
        return RendaTransf()
