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
        d['month'] = 'month'
        return d   