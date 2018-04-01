from datetime import date
from datetime import datetime
from test.GenericTest import GenericTest
from dao.DespesaTempDAO import DespesaTempDAO
from dao.PagamentoDAO import PagamentoDAO
from models.Despesa import Despesa
from models.DespesaTemp import DespesaTemp
from models.Pagamento import Pagamento

class PagamentoDAOTest(GenericTest):

    despesaTempDAO = DespesaTempDAO()
    pagamentoDAO = PagamentoDAO()

    def test(self):
        self.testAdd()
        self.testFind()
        self.testUpdate()
        self.testDelete()

    def testAdd(self):
        # add test row 1
        despesaTemp = self.getDespesaTempFilterModel1()
        despesaTemp.despesa.val = 1800
        despesaTemp.despesa.paidVal = 500
        despesaTemp.despesa.paid = 0
        despesaTemp.months = 5
        despesaTemp.paidMonths = 2

        self.despesaTempDAO.add(despesaTemp)

        print(self.findDespesaTemp1())
        despesaTemp = self.findDespesaTemp1()[0]

        self.createAndAddPagamentos(despesaTemp)

        # add test row 2
        despesaTemp = self.getDespesaTempFilterModel2()
        despesaTemp.despesa.val = 1900
        despesaTemp.despesa.paidVal = 600
        despesaTemp.despesa.paid = 0
        despesaTemp.months = 6
        despesaTemp.paidMonths = 3

        self.despesaTempDAO.add(despesaTemp)

        despesaTemp = self.findDespesaTemp2()[1]

        self.createAndAddPagamentos(despesaTemp)

        print(self.getJustifiedSuccessMsg('add'))

    def testFind(self):
        #find test row 1
        result = self.findDespesaTemp1()
        assert len(result) == 1, "there must be 1 DespesaTemp row"
        assert type(result[0]).__name__ == 'DespesaTemp', "Result type must be DespesaTemp"

        despesaTemp = result[0]
        print('despesaTemp id: ' + str(despesaTemp.despesa.id))
        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        assert len(pagamentos) == 3, "there must be 3 Pagamentos. There are {}.".format(len(pagamentos))
        
        #tmp
        for pagamento in pagamentos:
            print('pag despesa id: ' + str(pagamento.despesaTemp.despesa.id))
            print('month: ' + pagamento.month)

        month = datetime.strptime(despesaTemp.despesa.month, '%Y-%m-%d').date()
        for i in range(3):
            pmonth = date(month.year, month.month + i, month.day)
            pagamento = pagamentos[i]
            assert pagamento.despesaTemp.despesa.month == str(month), "Resulting row must be month {}, not {}".format(despesaFilter.despesa.month, month)
            assert pagamento.val == i, "val must be {}".format(i)
            assert pagamento.paid == 0, "paid must be 0"
            assert pagamento.month == str(pmonth), "month must be {}, not {}".format(pmonth, pagamento.month)

        #find test row 2
        result = self.findDespesaTemp2()
        assert len(result) == 2, "there must be 1 DespesaTemp row"
        assert type(result[1]).__name__ == 'DespesaTemp', "Result type must be DespesaTemp"

        despesaTemp = result[1]
        print('despesaTemp id: ' + str(despesaTemp.despesa.id))
        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        assert len(pagamentos) == 3, "there must be 3 Pagamentos. There are {}.".format(len(pagamentos))

        month = datetime.strptime(despesaTemp.despesa.month, '%Y-%m-%d').date()
        for i in range(3):
            pmonth = date(month.year, month.month + i, month.day)
            pagamento = pagamentos[i]
            print(pagamento)
            assert pagamento.despesaTemp.despesa.month == str(month), "Resulting row must be month {}, not {}".format(despesaFilter.despesa.month, month)
            assert pagamento.val == i, "val must be {}".format(i)
            assert pagamento.paid == 0, "paid must be 0"
            assert pagamento.month == str(pmonth), "month must be {}, not {}".format(pmonth, pagamento.month)

        print(self.getJustifiedSuccessMsg("find"))

    def testUpdate(self):

        # update one despesa temp's pagamentos. The other despesa temp's pagamentos
        # must be unchanged
        result = self.findDespesaTemp1()
        despesaTemp = result[0]
        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        pagamento = pagamentos[0]
        pagamento.val = 100
        pagamento.paid = 1
        self.pagamentoDAO.update(pagamento)

        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        assert pagamentos[0].val == 100 and pagamentos[0].paid == 1, "pagamento val and paid must be {} and {}".format(100, 1)
        assert pagamentos[1].val == 1 and pagamentos[1].paid == 0, "pagamento val and paid must be {} and {}".format(1, 0)
        assert pagamentos[2].val == 2 and pagamentos[2].paid == 0, "pagamento val and paid must be {} and {}".format(2, 0)

        result = self.findDespesaTemp2()
        despesaTemp = result[1]
        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))

        for i in range(3):
            assert pagamentos[i].val == i and pagamentos[i].paid == 0, "pagamentos val and paid must be {} and {}".format(i, 0)

        print(self.getJustifiedSuccessMsg("update"))

    def testDelete(self):
        # delete one despesa temp's pagamentos. The other despesa temp's pagamentos
        # must still be there
        result = self.findDespesaTemp1()
        despesaTemp = result[0]
        self.pagamentoDAO.delete(Pagamento(despesaTemp = despesaTemp))
        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        assert len(pagamentos) == 0, "there must be no pagamentos. They have been deleted."

        self.despesaTempDAO.delete(despesaTemp)
        result = self.findDespesaTemp1()
        assert len(result) == 0, "there must be no despesa temp with id {}".format(despesaTemp.despesa.id)

        # the other despesa temp's pagamentos should still be there
        result = self.findDespesaTemp2()
        despesaTemp = result[0]
        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        assert len(pagamentos) == 3, "there must be 3 pagamentos. Deleting the other despesa temp's pagamentos should not have deleted this one's"

        # now remove the other despesa temp's pagamentos
        self.pagamentoDAO.delete(Pagamento(despesaTemp = despesaTemp))
        pagamentos = self.pagamentoDAO.find(Pagamento(despesaTemp = despesaTemp))
        assert len(pagamentos) == 0, "there must be no pagamentos."

        self.despesaTempDAO.delete(despesaTemp)
        result = self.findDespesaTemp2()
        assert len(result) == 0, "there must be no despesa temp with id {}".format(despesaTemp.despesa.id)

        print(self.getJustifiedSuccessMsg("Delete"))

    def findDespesaTemp1(self):
        return self.despesaTempDAO.find(self.getDespesaTempFilterModel1())

    def findDespesaTemp2(self):
        return self.despesaTempDAO.find(self.getDespesaTempFilterModel2())

    #TODO find pagamentos

    def getDespesaTempFilterModel1(self):
        return DespesaTemp(despesa = Despesa(desc = 'desp test', month = '2018-02-01'))

    def getDespesaTempFilterModel2(self):
        return DespesaTemp(despesa = Despesa(desc = 'desp test', month = '2018-03-01'))

    def getPagamentoFilterModel1(self):
        return Pagamento(despesaTemp = getDespesaTempFilterModel1())

    def getPagamentoFilterModel2(self):
        return Pagamento(despesaTemp = getDespesaTempFilterModel2())

    # creates and adds (persists) pagamentos for three months beginning the month of the despesa temp
    def createAndAddPagamentos(self, despesaTemp):
        month = datetime.strptime(despesaTemp.despesa.month, '%Y-%m-%d').date()
        for i in range(3):
            pmonth = date(month.year, month.month + i, month.day)
            p = Pagamento(despesaTemp = despesaTemp, val = i, paid = 0, month = pmonth)
            self.pagamentoDAO.add(p)
