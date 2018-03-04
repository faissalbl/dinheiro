from datetime import date
from datetime import datetime
from test.GenericTest import GenericTest
from dao.DespesaTempDAO import DespesaTempDAO
from dao.PagamentoDAO import PagamentoDAO
from models.Despesa import Despesa
from models.DespesaTemp import DespesaTemp
from models.Pagamento import Pagamento

class DespesaTempDAOTest(GenericTest):

    despesaTempDAO = DespesaTempDAO()
    pagamentoDAO = PagamentoDAO()

    def test(self):
        self.testAdd()
        self.testFind()
        self.testUpdate()
        self.testDelete()

    def testAdd(self):
        # add test row 1
        despesaTemp = self.getTestRowFilterModel1()
        despesaTemp.despesa.val = 1800
        despesaTemp.despesa.paidVal = 500
        despesaTemp.despesa.paid = 0
        despesaTemp.months = 5
        despesaTemp.paidMonths = 2

        self.createPagamentos(despesaTemp)

        self.despesaTempDAO.add(despesaTemp)

        # add test row 2
        despesaTemp = self.getTestRowFilterModel2()
        despesaTemp.despesa.val = 1900
        despesaTemp.despesa.paidVal = 600
        despesaTemp.despesa.paid = 0
        despesaTemp.months = 6
        despesaTemp.paidMonths = 3

        print('despesaTemp {}, pagamentos {}'.format('[no id]', len(despesaTemp.pagamentos)))

        self.createPagamentos(despesaTemp)

        print('despesaTemp {}, pagamentos {}'.format('[no id]', len(despesaTemp.pagamentos)))

        self.despesaTempDAO.add(despesaTemp)

        print(self.getJustifiedSuccessMsg('add'))

    def testFind(self):
        #find test row 1
        result = self.findTestRow1()
        assert len(result) == 1, "there must be 1 DespesaTemp row"
        assert type(result[0]).__name__ == 'DespesaTemp', "Result type must be DespesaTemp"
        assert result[0].despesa.desc == 'desp test', "Resulting row must be desc 'desp test'"
        assert result[0].despesa.id, "id must be filled in"
        assert result[0].despesa.val == 1800 and result[0].despesa.paidVal == 500 and result[0].despesa.paid == 0 and result[0].months == 5 and result[0].paidMonths == 2, "val, paidVal, paid, month, paidMonths must be 1800, 500, 0, 5, 2"

        # check pagamentos
        pagamentos = result[0].pagamentos
        assert len(pagamentos) == 3, "there must be 3 pagamentos"
        assert pagamentos[0].val == 0 and pagamentos[0].paid == 0, "pagamento val and paid must be {} and {}".format(100, 1)
        assert pagamentos[1].val == 1 and pagamentos[1].paid == 0, "pagamento val and paid must be {} and {}".format(1, 0)
        assert pagamentos[2].val == 2 and pagamentos[2].paid == 0, "pagamento val and paid must be {} and {}".format(2, 0)

        #find test row 2
        result = self.findTestRow2()
        assert len(result) == 2, "there must be 2 DespesaTemp row"
        assert type(result[1]).__name__ == 'DespesaTemp', "Result type must be DespesaTemp"
        assert result[1].despesa.desc == 'desp test', "Resulting row must be desc 'desp test'"
        assert result[1].despesa.id, "id must be filled in"
        assert result[1].despesa.val == 1900 and result[1].despesa.paidVal == 600 and result[1].despesa.paid == 0 and result[1].months == 6 and result[1].paidMonths == 3, "val, paidVal, paid, month, paidMonths must be 1900, 600, 0, 6, 3"

        # check pagamentos
        pagamentos = result[1].pagamentos
        assert len(pagamentos) == 3, "there must be 3 pagamentos. There are {}".format(len(pagamentos))
        assert pagamentos[0].val == 0 and pagamentos[0].paid == 0, "pagamento val and paid must be {} and {}".format(0, 0)
        assert pagamentos[1].val == 1 and pagamentos[1].paid == 0, "pagamento val and paid must be {} and {}".format(1, 0)
        assert pagamentos[2].val == 2 and pagamentos[2].paid == 0, "pagamento val and paid must be {} and {}".format(2, 0)

        print(self.getJustifiedSuccessMsg("find"))

    def testUpdate(self):
        # find and update test row
        result = self.findTestRow1()
        model = result[0]
        newVal = 1300
        newMonths = 10
        newPaidMonths = 5
        model.despesa.val = newVal
        model.months = newMonths
        model.paidMonths = newPaidMonths

        # update one pagamento
        model.pagamentos[0].val = 100
        model.pagamentos[0].paid = 1

        self.despesaTempDAO.update(model)
        
        # find and validate updated test row
        result = self.findTestRow1()
        model = result[0]
        assert model.despesa.val == newVal and model.months == newMonths and model.paidMonths == newPaidMonths, "Val, months, paidMonths should be {}, {}, {}".format(newVal, newMonths, newPaidMonths)

        # check pagamentos
        pagamentos = model.pagamentos
        assert len(pagamentos) == 3, "there must be 3 pagamentos"
        assert pagamentos[0].val == 100 and pagamentos[0].paid == 1, "pagamento val and paid must be {} and {}".format(100, 1)
        assert pagamentos[1].val == 1 and pagamentos[1].paid == 0, "pagamento val and paid must be {} and {}".format(1, 0)
        assert pagamentos[2].val == 2 and pagamentos[2].paid == 0, "pagamento val and paid must be {} and {}".format(2, 0)    

        # check that data for the test row 2 remains the same
        result = self.findTestRow2()
        model = result[1]
        print(model.months)
        assert model.despesa.val == 1900 and model.months == 6 and model.paidMonths == 3, "Val, months, paidMonths should be {}, {}, {}".format(1900, 6, 3)

        assert result[1].despesa.desc == 'desp test', "Resulting row must be desc 'desp test'"
        assert result[1].despesa.id, "id must be filled in"
        assert result[1].despesa.val == 1900 and result[1].despesa.paidVal == 600 and result[1].despesa.paid == 0 and result[1].months == 6 and result[1].paidMonths == 3, "val, paidVal, paid, month, paidMonths must be 1900, 600, 0, 6, 3"

        # check pagamentos
        pagamentos = result[1].pagamentos
        assert len(pagamentos) == 3, "there must be 3 pagamentos"
        assert pagamentos[0].val == 0 and pagamentos[0].paid == 0, "pagamento val and paid must be {} and {}".format(0, 0)
        assert pagamentos[1].val == 1 and pagamentos[1].paid == 0, "pagamento val and paid must be {} and {}".format(1, 0)
        assert pagamentos[2].val == 2 and pagamentos[2].paid == 0, "pagamento val and paid must be {} and {}".format(2, 0)

        print(self.getJustifiedSuccessMsg("update"))

    def testDelete(self):
        # delete test row 1
        despesaTemp = self.findTestRow1()[0]
        self.despesaTempDAO.delete(despesaTemp)
        result = self.findTestRow1()
        assert len(result) == 0, "there must be 0 DespesaTemp row"

        # check that pagamentos for test row 1 were deleted
        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        assert len(pagamentos) == 0, "there must be 0 Pagamentos"

        # check that pagamentos for test row 2 are still there
        despesaTemp = self.findTestRow2()[0]

        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        assert len(pagamentos) == 3, "there must be 3 Pagamentos"

        # delete test row 2
        self.despesaTempDAO.delete(despesaTemp)
        result = self.findTestRow2()
        assert len(result) == 0, "there must be 0 DespesaTemp row"

        # check that pagamentos for test row 2 were deleted
        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        assert len(pagamentos) == 0, "there must be 0 Pagamentos"

        print(self.getJustifiedSuccessMsg("Delete"))

    def findTestRow1(self):
        return self.despesaTempDAO.find(self.getTestRowFilterModel1())

    def findTestRow2(self):
        return self.despesaTempDAO.find(self.getTestRowFilterModel2())

    def getTestRowFilterModel1(self):
        return DespesaTemp(despesa = Despesa(desc = 'desp test', month = '2018-02-01'))

    def getTestRowFilterModel2(self):
        return DespesaTemp(despesa = Despesa(desc = 'desp test', month = '2018-03-01'))

    # creates pagamentos for despesaTemp for three months beginning the month of the despesa temp
    def createPagamentos(self, despesaTemp):
        month = datetime.strptime(despesaTemp.despesa.month, '%Y-%m-%d').date()
        for i in range(3):
            pmonth = date(month.year, month.month + i, month.day)
            p = Pagamento(despesaTemp = despesaTemp, val = i, paid = 0, month = pmonth)
            despesaTemp.pagamentos.append(p)