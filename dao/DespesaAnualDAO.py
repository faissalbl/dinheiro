import os
from dao.GenericDAO import GenericDAO
from transforms.DespesaAnualTransf import DespesaAnualTransf
from models.Renda import Renda

class DespesaAnualDAO(GenericDAO):

    def getTransform(self):
        return DespesaAnualTransf()
