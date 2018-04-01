from datetime import date
from models.DespesaChild import DespesaChild
from collections import OrderedDict

class DespesaAnual(DespesaChild):
    
    def __init__(self, despesa = None):
        super().__init__(despesa)

    def __str__(self):
        return "DespesaAnual [despesa: {}]".format(self.despesa)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d.update(super().getPropertyToColumnDict())
        return d     