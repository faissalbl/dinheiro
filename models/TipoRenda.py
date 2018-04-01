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

    def defOutputStr(self):
        result = (self.id or '').ljust(9, ' ')
        result += (self.desc or '').ljust(20, ' ')
        result += str(self.auto if self.auto != None else '').rjust(4, ' ').ljust(6, ' ')
        return result

    def defOutputStrHeader(self):
        result = 'ID'.ljust(9, ' ')
        result += 'DESC'.ljust(20, ' ')
        result += 'AUTO'.rjust(4, ' ').ljust(6, ' ')
        return result
