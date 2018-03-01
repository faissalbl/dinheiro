from models.GenericModel import GenericModel
from models.TipoRenda import TipoRenda
from collections import OrderedDict

class Renda(GenericModel):

    def __init__(self, tipoRenda = None, val = None, month = None):
        self.tipoRenda = tipoRenda
        self.val = val
        self.month = month

    def __str__(self):
        return "Renda [tipoRendaId: {}, val: {}, month: {}]".format(self.tipoRenda.id if self.tipoRenda else '', self.val, self.month)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['tipoRenda.id'] = 'tipo_renda_id'
        d['val'] = 'val'
        d['month'] = 'month'
        return d        