from test.GenericTest import GenericTest
from dao.DespesaAnualDAO import DespesaAnualDAO
from models.Despesa import Despesa
from models.DespesaAnual import DespesaAnual

class DespesaAnualDAOTest(GenericTest):

    despesaAnualDAO = DespesaAnualDAO()

    def test(self):
        self.testAdd()
        self.testFind()
        self.testUpdate()
        self.testDelete()

    def testAdd(self):
        # add test row 1
        despesaAnual = self.getTestRowFilterModel1()
        despesaAnual.despesa.val = 1800
        despesaAnual.despesa.paidVal = 500
        despesaAnual.despesa.paid = 0

        self.despesaAnualDAO.add(despesaAnual)

        # add test row 2
        despesaAnual = self.getTestRowFilterModel2()
        despesaAnual.despesa.val = 1900
        despesaAnual.despesa.paidVal = 600
        despesaAnual.despesa.paid = 0

        self.despesaAnualDAO.add(despesaAnual)

        print(self.getJustifiedSuccessMsg('add'))

    def testFind(self):
        #find test row 1
        result = self.findTestRow1()
        print (result[0])
        assert len(result) == 1, "there must be 1 DespesaAnual row"
        assert type(result[0]).__name__ == 'DespesaAnual', "Result type must be DespesaAnual"
        assert result[0].despesa.desc == 'desp test', "Resulting row must be desc 'desp test'"
        assert result[0].despesa.id, "id must be filled in"
        assert result[0].despesa.val == 1800 and result[0].despesa.paidVal == 500 and result[0].despesa.paid == 0, "val, paidVal, paid must be 1800, 500, 0"

        #find test row 1
        result = self.findTestRow2()
        print (result[0])
        assert len(result) == 1, "there must be 1 DespesaAnual row"
        assert type(result[0]).__name__ == 'DespesaAnual', "Result type must be DespesaAnual"
        assert result[0].despesa.desc == 'desp test', "Resulting row must be desc 'desp test'"
        assert result[0].despesa.id, "id must be filled in"
        assert result[0].despesa.val == 1900 and result[0].despesa.paidVal == 600 and result[0].despesa.paid == 0, "val, paidVal, paid must be 1900, 600, 0"

        print(self.getJustifiedSuccessMsg("find"))

    def testUpdate(self):
        # find and update test row
        result = self.findTestRow1()
        model = result[0]
        newVal = 1300
        model.despesa.val = newVal
        self.despesaAnualDAO.update(model)
        
        # find and validate updated test row
        result = self.findTestRow1()
        model = result[0]
        print(model)
        assert model.despesa.val == newVal, "Val should be {}".format(newVal)
        print(self.getJustifiedSuccessMsg("update"))

    def testDelete(self):
        # delete test row 1
        self.despesaAnualDAO.delete(self.findTestRow1()[0])
        result = self.findTestRow1()
        assert len(result) == 0, "there must be 0 DespesaAnual row"

        # delete test row 2
        self.despesaAnualDAO.delete(self.findTestRow2()[0])
        result = self.findTestRow2()
        assert len(result) == 0, "there must be 0 DespesaAnual row"

        print(self.getJustifiedSuccessMsg("Delete"))

    def findTestRow1(self):
        return self.despesaAnualDAO.find(self.getTestRowFilterModel1())

    def findTestRow2(self):
        return self.despesaAnualDAO.find(self.getTestRowFilterModel2())

    def getTestRowFilterModel1(self):
        return DespesaAnual(despesa = Despesa(desc = 'desp test', month = '2018-02-01'))

    def getTestRowFilterModel2(self):
        return DespesaAnual(despesa = Despesa(desc = 'desp test', month = '2018-03-01'))
