from models.GenericModel import GenericModel
from collections import OrderedDict

class Despesa(GenericModel):

    def __init__(self, id = None, desc = None, val = None, paidVal = None, paid = None, month = None):
        self.id = id
        self.desc = desc
        self.val = val
        self.paidVal = paidVal
        self.paid = paid
        self.month = month

    def __str__(self):
        return "[id: {}, desc: {}, val: {}, paidVal: {}, paid: {}, month: {}]".format(
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
