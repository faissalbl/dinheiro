import os
from dao.GenericDAO import GenericDAO
from transforms.DespesaTempTransf import DespesaTempTransf

class DespesaChildDAO(GenericDAO):

    # adds despesa and despesa temp
    def add(self, model):
        despesaId = super().add(model.despesa)
        model.despesa.id = despesaId

        return super().add(model)

    # updates despesa and despesa temp
    def update(self, model):
        super().update(model.despesa)
        super().update(model)

    # delete despesa temp and despesa
    def delete(self, model):
        super().delete(model)
        super().delete(model.despesa)

    def getTransform(self):
        return DespesaChildTransf()