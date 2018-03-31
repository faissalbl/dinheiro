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
        d['month.id'] = 'month_id'
        d['taxable'] = 'taxable'
        return d   

    def setMonth(self, month):
        self.month = month     

    def getMonth(self):
        return self.month

    def defOutputStr(self):
        result = self.tipoRenda.defOutputStr()
        result += ('%.2f' % self.val).rjust(8, ' ').ljust(10, ' ')
        result += str(self.month.month).ljust(12, ' ')
        result += str(self.taxable).rjust(7, ' ').ljust(9, ' ')
        return result

    def defOutputStrHeader(self):
        result = self.tipoRenda.defOutputStrHeader()
        result += 'VAL'.rjust(8, ' ').ljust(10, ' ')
        result += 'MONTH'.ljust(12, ' ')
        result += 'TAXABLE'.rjust(7, ' ').ljust(9, ' ')
        return result
