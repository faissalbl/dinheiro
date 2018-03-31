from models.GenericModel import GenericModel
from collections import OrderedDict

class CarneLeao(GenericModel):

    def __init__(self, month = None, income = None, tax = None, paid = None):
        self.month = month
        self.income = income
        self.tax = tax
        self.paid = paid

    def __str__(self):
        return "CarneLeao [month: {}, income: {}, tax: {}, paid: {}]".format(
            self.month, self.income, self.tax, self.paid)

    def getPropertyToColumnDict(self):
        d = OrderedDict()
        d['month.id'] = 'month_id'
        d['income'] = 'income'
        d['tax'] = 'tax'
        d['paid'] = 'paid'
        return d   

    def setMonth(self, month):
        self.month = month     

    def getMonth(self):
        return self.month