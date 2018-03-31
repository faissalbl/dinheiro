from models.GenericModel import GenericModel
from collections import OrderedDict

class Month(GenericModel):

    def __init__(self, id = None, month = None, user = None):
        self.id = id
        self.month = month
        self.user = user

    def __str__(self):
        return "Month [id: {}, month: {}, user: {}]".format(
            self.id,
            self.month, 
            self.user)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['id'] = 'id'
        d['month'] = 'month'
        d['user'] = 'user'
        return d   

    def setMonth(self, month):
        pass     