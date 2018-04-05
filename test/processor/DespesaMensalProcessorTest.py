from test.GenericTest import GenericTest
from processor.DespesaMensalProcessor import DespesaMensalProcessor
from processor.RendaProcessor import RendaProcessor
from processor.MonthProcessor import MonthProcessor
from models.Despesa import Despesa
from models.DespesaMensal import DespesaMensal
from datetime import date

class DespesaMensalProcessorTest(GenericTest):

    def __init__(self, month):
        super().__init__(month)

    def testBody(self):
        self.despesaMensalProcessor = DespesaMensalProcessor(month = self.month)
        self.despesaMensalFilter = DespesaMensal(despesa = Despesa(month = self.month))
        self.testAdd()
        self.testUpdate()
        self.testDelete()        

    def testAdd(self):
        for i in range(2):
            despesa = Despesa(desc = 'Test {}'.format(i + 1), val = 1000, paidVal = 500, paid = 0, month = self.month)
            despesaMensal = DespesaMensal(despesa = despesa, auto = 0)
            self.despesaMensalProcessor.add(despesaMensal)

        result = self.despesaMensalProcessor.find()
        assert len(result) == 2, 'there must be 2 despesas mensais'

        for despesaMensal in result:
            assert despesaMensal.despesa.id, 'despesa mensal expected id must not be null'
            assert despesaMensal.despesa.desc in ('Test 1', 'Test 2'), 'desc must be {}, not {}'.format('Test 1 or Test 2', despesaMensal.despesa.desc) 
            assert despesaMensal.despesa.val == 1000, 'val must be {}, not {}'.format(1000, despesaMensal.despesa.val)
            assert despesaMensal.despesa.paidVal == 500, 'paidVal must be {}, not {}'.format(500, despesaMensal.despesa.paidVal)
            assert despesaMensal.despesa.month.id == self.month.id, 'month.id must be {}, not {}'.format(self.month.id, despesaMensal.despesa.month.id)

        print(self.getJustifiedSuccessMsg('add'))

    def testUpdate(self):
        result = self.despesaMensalProcessor.find()

        despesaMensal = result[0]
        despesaId = despesaMensal.despesa.id

        # update
        newVal = 500
        newPaidVal = 300
        despesaMensal.despesa.val = newVal
        despesaMensal.despesa.paidVal = newPaidVal

        self.despesaMensalProcessor.update(despesaMensal)

        result = self.despesaMensalProcessor.find()
        
        for despesaMensal in result:
            if despesaMensal.despesa.id == despesaId:
                assert despesaMensal.despesa.val == newVal and despesaMensal.despesa.paidVal == newPaidVal, 'val and paidVal must be {}, {}, but resulting despesa mensal is {}'.format(val, paidVal, despesaMensal)
            else:
                assert despesaMensal.despesa.val != newVal and despesaMensal.despesa.paidVal != newPaidVal, 'val and paidVal should not be {}, {}, but resulting despesa mensal is {}'.format(val, paidVal, despesaMensal)    

        print(self.getJustifiedSuccessMsg('update'))
    