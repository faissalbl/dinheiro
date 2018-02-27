from dao.DespesaChildDAO import DespesaChildDAO
from transforms.DespesaAnualTransf import DespesaAnualTransf

class DespesaAnualDAO(DespesaChildDAO):

    def getTransform(self):
        return DespesaAnualTransf()
