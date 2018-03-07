from models.GenericModel import GenericModel
from collections import OrderedDict

class TipoRenda(GenericModel):

    def __init__(self, id = None, desc = None, auto = None):
        self.id = id
        self.desc = desc
        self.auto = auto

    def setMonth(self, month):
        pass

    def __str__(self):
        return "TipoRenda [id: {}, desc: {}, auto: {}]".format(self.id, self.desc, self.auto)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['id'] = 'id'
        d['desc'] = 'desc'
        d['auto'] = 'auto'
        return d        
