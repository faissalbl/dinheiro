from datetime import date
from datetime import datetime

class GenericProcessor:

    def getCurrentMonth(self):
        today = date.today()
        return date(today.year, today.month, 1)