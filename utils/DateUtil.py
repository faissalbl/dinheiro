from datetime import date
from datetime import datetime
from datetime import timedelta

def previousMonth(month):
    month = toDate(month)
    previousMonth = month - timedelta(days = 1)
    previousMonth = previousMonth.replace(day = 1)
    return previousMonth

def nextMonth(month):
    # this will always take the month to the next month
    month = toDate(month)
    nextMonth = month.replace(day = 28) + timedelta(days = 4)
    nextMonth = nextMonth.replace(day = 1)
    return nextMonth

def toDate(strDate):
    result = strDate
    if strDate and type(strDate).__name__ != 'date':
        result = datetime.strptime(strDate, '%Y-%m-%d').date()

    return result
