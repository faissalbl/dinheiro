from models.GenericModel import GenericModel
from models.TipoRenda import TipoRenda
from collections import OrderedDict

class Renda(GenericModel):

    def __init__(self, tipoRenda = None, val = None, month = None, taxable = None):
        self.tipoRenda = tipoRenda if tipoRenda else TipoRenda()
        self.val = val
        self.month = month
        self.taxable = taxable

    def __str__(self):
        return "Renda [tipoRendaId: {}, val: {}, month: {}, taxable: {}]".format(
            self.tipoRenda.id if self.tipoRenda else '', self.val, self.month, self.taxable)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['tipoRenda.id'] = 'tipo_renda_id'
        d['tipoRenda.auto'] = 'auto'
        d['val'] = 'val'
        d['month'] = 'month'
        d['taxable'] = 'taxable'
        return d   

    def setMonth(self, month):
        self.month = month     