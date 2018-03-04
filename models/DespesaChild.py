from models.GenericModel import GenericModel
from models.Despesa import Despesa
from collections import OrderedDict

class DespesaChild(GenericModel):

    def __init__(self, despesa = None):
        self.despesa = despesa if despesa != None else Despesa()

    def setMonth(self, month):
        self.despesa.month = month