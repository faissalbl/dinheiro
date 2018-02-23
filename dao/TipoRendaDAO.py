import os
from dao.GenericDAO import GenericDAO
from transforms.TipoRendaTransf import TipoRendaTransf

class TipoRendaDAO(GenericDAO):

    def getTransform(self):
        return TipoRendaTransf()
