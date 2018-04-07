from test.GenericTest import GenericTest
from processor.DespesaMensalProcessor import DespesaMensalProcessor
from processor.DespesaAnualProcessor import DespesaAnualProcessor
from processor.RendaProcessor import RendaProcessor
from processor.MonthProcessor import MonthProcessor
from models.Despesa import Despesa
from models.DespesaMensal import DespesaMensal
from models.DespesaAnual import DespesaAnual
from models.Renda import Renda
from datetime import date

class DespesaAnualProcessorTest(GenericTest):

    def __init__(self, month):
        super().__init__(month)

    def testBody(self):
        self.despesaMensalProcessor = DespesaMensalProcessor(month = self.month)
        self.despesaAnualProcessor = DespesaAnualProcessor(month = self.month)
        self.rendaProcessor = RendaProcessor(month = self.month)

        self.despesaMensalFilter = DespesaMensal(despesa = Despesa(month = self.month))
        self.despesaAnualFilter = DespesaAnual(despesa = Despesa(month = self.month))
        self.rendaFilter = Renda(month = self.month)

        self.testAdd()
        self.testUpdate()
        self.testDelete()        

    def testAdd(self):
        val = 1000
        totalAnual = 0.0
        for i in range(2):
            despesa = Despesa(desc = 'Test {}'.format(i + 1), val = val, paidVal = 500, paid = 0, month = self.month)
            despesaAnual = DespesaAnual(despesa = despesa)
            self.despesaAnualProcessor.add(despesaAnual)
            totalAnual += val

        result = self.despesaAnualProcessor.find()
        assert len(result) == 2, 'there must be 2 despesas anuais'

        for despesaAnual in result:
            assert despesaAnual.despesa.id, 'despesa expected id must not be null'
            assert despesaAnual.despesa.desc in ('Test 1', 'Test 2'), 'desc must be {}, not {}'.format('Test 1 or Test 2', despesaAnual.despesa.desc) 
            assert despesaAnual.despesa.val == 1000, 'val must be {}, not {}'.format(1000, despesaAnual.despesa.val)
            assert despesaAnual.despesa.paidVal == 500, 'paidVal must be {}, not {}'.format(500, despesaAnual.despesa.paidVal)
            assert despesaAnual.despesa.month.id == self.month.id, 'month.id must be {}, not {}'.format(self.month.id, despesaAnual.despesa.month.id)

        self.testAfterAddUpdate(totalAnual)

        print(self.getJustifiedSuccessMsg('add'))

    def testUpdate(self):
        result = self.despesaAnualProcessor.find()

        despesaAnual = result[0]
        despesaId = despesaAnual.despesa.id

        # update
        newVal = 500
        newPaidVal = 300
        despesaAnual.despesa.val = newVal
        despesaAnual.despesa.paidVal = newPaidVal

        self.despesaAnualProcessor.update(despesaAnual)

        result = self.despesaAnualProcessor.find()
        
        totalAnual = 0.0
        for despesaAnual in result:
            totalAnual += despesaAnual.despesa.val
            if despesaAnual.despesa.id == despesaId:
                assert despesaAnual.despesa.val == newVal and despesaAnual.despesa.paidVal == newPaidVal, 'val and paidVal must be {}, {}, but resulting despesa anual is {}'.format(val, paidVal, despesaAnual)
            else:
                assert despesaAnual.despesa.val != newVal and despesaAnual.despesa.paidVal != newPaidVal, 'val and paidVal should not be {}, {}, but resulting despesa anual is {}'.format(val, paidVal, despesaAnual)    

        self.testAfterAddUpdate(totalAnual)

        print(self.getJustifiedSuccessMsg('update'))
    
    def testDelete(self):
        result = self.despesaAnualProcessor.find()
        assert len(result) == 2, 'there must be 2 despesas anuais'

        for despesaAnual in result:
            self.despesaAnualProcessor.delete(despesaAnual)

        result = self.despesaAnualProcessor.find()
        assert len(result) == 0, 'there must be no despesas anuais'

        # a despesa mensal 'Reserva' must have been created when despesas anuais were created
        result = self.despesaMensalProcessor.find()
        assert len(result) == 1, 'there must be one and only one despesa mensal'
        assert result[0].auto == 1, 'the despesa mensal created must be automatically calculated'

        self.despesaMensalProcessor.delete(result[0])
        result = self.despesaMensalProcessor.find()
        assert len(result) == 0, 'there must be no despesas mensais'

        # a renda 'Reserva' must have been created when despesas mensais were created
        result = self.rendaProcessor.find()
        assert len(result) == 1, 'there must be one and only one renda'
        assert result[0].tipoRenda.auto == 1, 'the renda created must be a automatically calculated type'

        self.rendaProcessor.delete(result[0])
        result = self.rendaProcessor.find()
        assert len(result) == 0, 'there must be no renda'

        print(self.getJustifiedSuccessMsg('delete'))

    def testAfterAddUpdate(self, totalDespesaAnual):
        # creating despesas anuais must have resulted in a despesa mensal 'reserva' being created
        result = self.despesaMensalProcessor.find()
        assert len(result) == 1, 'there must be 1 despesa mensal'
        despesaMensal = result[0]
        assert despesaMensal.despesa.id, 'despesa expected id must not be null'
        assert despesaMensal.despesa.desc == 'Reserva Anual', 'desc must be {}, not {}'.format('Test 1 or Test 2', despesaMensal.despesa.desc) 
        assert despesaMensal.auto == 1, 'auto must be {}, not {}'.format(1, despesaMensal.auto)
        expectedDespesaMensalVal = (totalDespesaAnual / 12.0)
        assert despesaMensal.despesa.val == expectedDespesaMensalVal, 'val must be {}, not {}'.format(expectedDespesaMensalVal, despesaMensal.despesa.val)
        assert despesaMensal.despesa.paidVal == None, 'paidVal must be {}, not {}'.format(None, despesaMensal.despesa.paidVal)
        assert despesaMensal.despesa.month.id == self.month.id, 'month.id must be {}, not {}'.format(self.month.id, despesaMensal.despesa.month.id)

        # despesa mensal having been created above triggers creation of a renda 'reserva'
        result = self.rendaProcessor.find()
        assert len(result) == 1
        renda = result[0]
        assert renda.tipoRenda.auto == 1, 'tipo renda auto must be {}, not {}'.format(1, renda.tipoRenda.auto)
        assert renda.val == expectedDespesaMensalVal, 'renda must have val {}, not {}'.format(expectedDespesaMensalVal, renda.val)

        print(self.getJustifiedSuccessMsg('after CRUD'))
