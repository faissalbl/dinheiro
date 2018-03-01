from test.GenericTest import GenericTest
from processor.GenericProcessor import GenericProcessor
from datetime import date

class GenericProcessorTest(GenericTest):

    def __init__(self):
        self.genericProcessor = GenericProcessor()

    def test(self):
        self.testMonth()
        self.testChangeMonth()

    def testMonth(self):
        today = date.today()
        expectedMonth = date(today.year, today.month, 1)

        month = self.genericProcessor.month

        assert month == expectedMonth, 'month {} must be equal to the expected month {}'.format(month, expectedMonth)

        print(self.getJustifiedSuccessMsg('month'))

    def testChangeMonth(self):
        today = date.today()
        expectedMonth = date(2020, 5, 1)

        self.genericProcessor.changeMonth('5/2020')
        month = self.genericProcessor.month
        assert month == expectedMonth, 'month {} must be equal to the expected month {}'.format(month, expectedMonth)

        self.genericProcessor.changeMonth('5/2020')
        month = self.genericProcessor.month
        assert month == expectedMonth, 'month {} must be equal to the expected month {}'.format(month, expectedMonth)

        self.genericProcessor.changeMonth('5/2020')
        month = self.genericProcessor.month
        assert month == expectedMonth, 'month {} must be equal to the expected month {}'.format(month, expectedMonth)
        
        self.genericProcessor.changeMonth('5/2020')
        month = self.genericProcessor.month
        assert month == expectedMonth, 'month {} must be equal to the expected month {}'.format(month, expectedMonth)

        print(self.getJustifiedSuccessMsg('changeMonth'))
