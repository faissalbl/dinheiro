from models.GenericModel import GenericModel
from collections import OrderedDict

class TipoRenda(GenericModel):
    id = None
    desc = None

    def __init__(self, id = None, desc = None):
        self.id = id
        self.desc = desc

    def __str__(self):
        return "[id: {}, desc: {}]".format(self.id, self.desc)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['id'] = 'id'
        d['desc'] = 'desc'
        return d        
