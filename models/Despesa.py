from models.GenericModel import GenericModel
from collections import OrderedDict

class Despesa(GenericModel):

    def __init__(self, id = None, desc = None, val = 0, paidVal = 0, paid = 0, month = None):
        self.id = id
        self.desc = desc
        self.val = float(val) if val != None else None
        self.paidVal = float(paidVal) if paidVal != None else None
        self.paid = int(paid) if paid != None else None
        self.month = month

    def __str__(self):
        return "Despesa [id: {}, desc: {}, val: {}, paidVal: {}, paid: {}, month: {}]".format(
            self.id, self.desc, self.val, self.paidVal, self.paid, self.month
        )

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['id'] = 'id'
        d['desc'] = 'desc'
        d['val'] = 'val'
        d['paidVal'] = 'paid_val'
        d['paid'] = 'paid'
        d['month.id'] = 'month_id'
        d['month.month'] = 'month'
        return d   

    def defOutputStr(self):
        result = str(self.id).rjust(6, ' ').ljust(8, ' ')
        result += self.desc.ljust(30, ' ')
        result += ('%.2f' % self.val).rjust(8, ' ').ljust(10, ' ')
        result += ('%.2f' % self.paidVal).rjust(8, ' ').ljust(10, ' ')
        result += str(self.paid).rjust(4, ' ').ljust(6, ' ')
        result += str(self.month.month).ljust(12, ' ')
        return result

    def defOutputStrHeader(self):
        result = 'ID'.rjust(6, ' ').ljust(8, ' ')
        result += 'DESC'.ljust(30, ' ')
        result += 'VAL'.rjust(8, ' ').ljust(10, ' ')
        result += 'PAID VAL'.rjust(8, ' ').ljust(10, ' ')
        result += 'PAID'.rjust(4, ' ').ljust(6, ' ')
        result += 'MONTH'.ljust(12, ' ')
        return result
