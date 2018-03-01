from datetime import date
import re

class GenericProcessor:

    def __init__(self):
        self.month = self.getCurrentMonth()

    def getCurrentMonth(self):
        today = date.today()
        return date(today.year, today.month, 1)

    def changeMonth(self, month):
        aMonth = re.split('/| |,|-', month)
        if len(aMonth) != 2:
            raise ValueError('{} is not a valid month format. Valid month formats look like: {}'.format(month, '\'02 2018\', \'02-2018\', \'02/2018\', \'02,2018\'')) 

        self.month = date(int(aMonth[1]), int(aMonth[0]), 1)