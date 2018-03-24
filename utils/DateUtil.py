from datetime import date
from datetime import timedelta

def previousMonth(month):
    month = month - timedelta(days = 1)
    month = month.replace(day = 1)
    return month