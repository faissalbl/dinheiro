import os
from dao.GenericDAO import GenericDAO
from transforms.DespesaTempTransf import DespesaTempTransf
from models.DespesaTemp import DespesaTemp

class DespesaTempDAO(GenericDAO):

    def getTransform(self):
        return DespesaTempTransf()
