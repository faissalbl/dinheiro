import os
from dao.GenericDAO import GenericDAO
from transforms.PagamentoTransf import PagamentoTransf
from models.Pagamento import Pagamento

class PagamentoDAO(GenericDAO):

    def getTransform(self):
        return PagamentoTransf()
