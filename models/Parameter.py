from models.GenericModel import GenericModel
from collections import OrderedDict

class Parameter(GenericModel):

    def __init__(self, namespace = None, name = None, val = None):
        self.namespace = namespace
        self.name = name
        self.val = val

    def __str__(self):
        return "Parameter [namespace: {}, name: {}, val: {}]".format(self.namespace, self.name, self.val)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['namespace'] = 'namespace'
        d['name'] = 'name'
        d['val'] = 'val'
        return d   

    def setMonth(self, month):
        pass     