from datetime import date
import re

class GenericProcessor:

    def __init__(self, mon = None):
        if mon == None:
            self.month = self.getCurrentMonth()
        else:
            self.changeMonth(mon)

    def getCurrentMonth(self):
        today = date.today()
        return date(today.year, today.month, 1)

    def changeMonth(self, month):
        aMonth = re.split('/| |,|-', month)
        if len(aMonth) != 2:
            raise ValueError('{} is not a valid month format. Valid month formats look like: {}'.format(month, '\'02 2018\', \'02-2018\', \'02/2018\', \'02,2018\'')) 

        self.month = date(int(aMonth[1]), int(aMonth[0]), 1)

    def getDAO(self):
        raise NotImplementedError('subclasses must implement this')

    def getModelType(self):
        raise NotImplementedError('this has not been implemented')

    def ls(self):
        model = self.getModelType()()
        model.setMonth(self.month)
        return self.getDAO().find(model)

    def add(self, model):
        model.setMonth(self.month)
        self.getDAO().add(model)

    def rm(self, model):
        model.setMonth(self.month)
        self.getDAO().delete(model)

