from utils import argparser 
from processor.MonthProcessor import MonthProcessor
from models.Month import Month

class GenericTest:

    def __init__(self, month):
        self.monthFilter = month
        if self.monthFilter:
            self.monthProcessor = MonthProcessor(self.monthFilter.user, month = self.monthFilter)

    def getJustifiedSuccessMsg(self, msg):
        success_msg = '{} -> {} {}'.format(self.getClassName(), msg, 'Success!'.rjust(70 - len(str(msg)), ' '))
        return success_msg

    def getClassName(self):
        return type(self).__name__  

    def test(self):
        self.testInit()
        self.testBody()
        self.testEnd()

    def testInit(self):
        self.monthProcessor.add(self.monthFilter)
        result = self.monthProcessor.find()
        self.month = None
        if len(result) == 1:
            self.month = result[0]
        assert self.month, 'month must not be null, it should have been persisted'
        assert self.month.id and self.month.month == '9999-01-01' and self.month.user == 'Test', 'month id, month and user must be: {}, {}, {}'.format(self.month.id, self.month.month, self.month.user)
        print(self.getJustifiedSuccessMsg('test init'))

    def testBody(self):
    	raise NotImplementedError('not implemented yet')

    def testEnd(self):
        self.monthProcessor.delete(self.month)
        result = self.monthProcessor.find()
        self.month = None
        if len(result) == 1:
            self.month = result[0]
        assert not self.month, 'month must be null, it should have been deleted'
        print(self.getJustifiedSuccessMsg('test end'))


