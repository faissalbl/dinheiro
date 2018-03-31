from datetime import date
import re
from processor.GenericProcessor import GenericProcessor
from models.Month import Month
from dao.MonthDAO import MonthDAO
from utils import DateUtil

class MonthProcessor(GenericProcessor):

    def __init__(self, month = None):
        if month and type(month).__name__ == 'Month':
            self.month = month
        else:
            self.month = Month()
            if not month:
                self.month.month = self.getCurrentMonth()
            elif type(month).__name__ == 'date':
                self.month.month = month.replace(day = 1)
            else:
                self.month.month = self.convertMonthInputDate(month)

        super().__init__(month = self.month)
        self.monthDAO = MonthDAO()
    
    def getDAO(self):
        return self.monthDAO

    def getModelType(self):
        return Month

    def convertMonthInputDate(self, month):
        print('month: {}'.format(month))
        aMonth = re.split('/| |,|-', month)
        if len(aMonth) != 2:
            raise ValueError('{} is not a valid month format. Valid month formats look like: {}'.format(month, '\'02 2018\', \'02-2018\', \'02/2018\', \'02,2018\'')) 

        return date(int(aMonth[1]), int(aMonth[0]), 1)

    def changeMonth(self, user):
        '''
            Changes the month and then copy despesas mensais from previous months if they
            don't exist.
        '''
        from processor.DespesaMensalProcessor import DespesaMensalProcessor
        monthFilter = Month(month = self.month.month, user = user)
        months = self.monthDAO.find(monthFilter)
        month = None
        if len(months) == 1:
            month = months[0]
        else:
            month = monthFilter
            monthId = self.monthDAO.add(month)
            month.id = monthId

            print('Copying despesas from the past months...')
            DespesaMensalProcessor(month = month).copy()
            print('...Done')

        despesaMensalProcessor = DespesaMensalProcessor(month = month)
        despesaMensalProcessor.updateDespReservaAnual()
        despesaMensalProcessor.updateDespCarneLeao()

        month.month = DateUtil.toDate(month.month)
        return month

    def getCurrentMonth(self):
        month = date.today()
        return month.replace(day = 1)

    def find(self):
        model = self.month
        return self.getDAO().find(model)

    def count(self):
        model = self.month
        return self.getDAO().count(model)

    def add(self, model):
        self.getDAO().add(model)
