from test.GenericTest import GenericTest
from dao.DespesaTempDAO import DespesaTempDAO
from models.Despesa import Despesa
from models.DespesaTemp import DespesaTemp

class DespesaTempDAOTest(GenericTest):

    despesaTempDAO = DespesaTempDAO()

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

        self.despesaTempDAO.add(despesaTemp)

        # add test row 2
        despesaTemp = self.getTestRowFilterModel2()
        despesaTemp.despesa.val = 1900
        despesaTemp.despesa.paidVal = 600
        despesaTemp.despesa.paid = 0
        despesaTemp.savedVal = 400
        despesaTemp.months = 6
        despesaTemp.paidMonths = 3

        self.despesaTempDAO.add(despesaTemp)

        print(self.getJustifiedSuccessMsg('add'))

    def testFind(self):
        #find test row 1
        result = self.findTestRow1()
        print (result[0])
        assert len(result) == 1, "there must be 1 DespesaTemp row"
        assert type(result[0]).__name__ == 'DespesaTemp', "Result type must be DespesaTemp"
        assert result[0].despesa.desc == 'desp test', "Resulting row must be desc 'desp test'"
        assert result[0].despesa.id, "id must be filled in"
        assert result[0].despesa.val == 1800 and result[0].despesa.paidVal == 500 and result[0].despesa.paid == 0 and result[0].months == 5 and result[0].paidMonths == 2, "val, paidVal, paid, month, paidMonths must be 1800, 500, 0, 300, 5, 2"

        #find test row 1
        result = self.findTestRow2()
        print (result[0])
        assert len(result) == 1, "there must be 1 DespesaTemp row"
        assert type(result[0]).__name__ == 'DespesaTemp', "Result type must be DespesaTemp"
        assert result[0].despesa.desc == 'desp test', "Resulting row must be desc 'desp test'"
        assert result[0].despesa.id, "id must be filled in"
        assert result[0].despesa.val == 1900 and result[0].despesa.paidVal == 600 and result[0].despesa.paid == 0 and result[0].months == 6 and result[0].paidMonths == 3, "val, paidVal, paid, month, paidMonths must be 1900, 600, 0, 400, 6, 3"

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
        self.despesaTempDAO.update(model)
        
        # find and validate updated test row
        result = self.findTestRow1()
        model = result[0]
        print(model)
        assert model.despesa.val == newVal and model.months == newMonths and model.paidMonths == newPaidMonths, "Val, months, paidMonths should be {}, {}, {}".format(newVal, months, paidMonths)
        print(self.getJustifiedSuccessMsg("update"))

    def testDelete(self):
        # delete test row 1
        self.despesaTempDAO.delete(self.findTestRow1()[0])
        result = self.findTestRow1()
        assert len(result) == 0, "there must be 0 DespesaTemp row"

        # delete test row 2
        self.despesaTempDAO.delete(self.findTestRow2()[0])
        result = self.findTestRow2()
        assert len(result) == 0, "there must be 0 DespesaTemp row"

        print(self.getJustifiedSuccessMsg("Delete"))

    def findTestRow1(self):
        return self.despesaTempDAO.find(self.getTestRowFilterModel1())

    def findTestRow2(self):
        return self.despesaTempDAO.find(self.getTestRowFilterModel2())

    def getTestRowFilterModel1(self):
        return DespesaTemp(despesa = Despesa(desc = 'desp test', month = '2018-02-01'))

    def getTestRowFilterModel2(self):
        return DespesaTemp(despesa = Despesa(desc = 'desp test', month = '2018-03-01'))
