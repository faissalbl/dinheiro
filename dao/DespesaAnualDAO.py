from dao.GenericDAO import GenericDAO
from dao.DespesaChildDAO import DespesaChildDAO
from transforms.DespesaAnualTransf import DespesaAnualTransf

class DespesaAnualDAO(DespesaChildDAO):

    # updates despesa
    def update(self, model):
        GenericDAO.update(self, model.despesa)

    def getTransform(self):
        return DespesaAnualTransf()
