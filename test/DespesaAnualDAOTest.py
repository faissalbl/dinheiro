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
        despesaAnual = self.getTestRowFilterModel()
        despesaAnual.despesa.val = 1800
        despesaAnual.despesa.paidVal = 500
        despesaAnual.despesa.paid = 0
        despesaAnual.savedVal = 300

        self.despesaAnualDAO.add(despesaAnual)
        print(self.getJustifiedSuccessMsg('add'))

    def testFind(self):
        result = self.findTestRow()
        print (result[0])
        assert len(result) == 1, "there must be 1 DespesaAnual row"
        assert type(result[0]).__name__ == 'DespesaAnual', "Result type must be DespesaAnual"
        assert result[0].despesa.desc == 'desp test', "Resulting row must be desc 'desp test'"
        assert result[0].despesa.id, "id must be filled in"
        assert result[0].despesa.val == 1800 and result[0].despesa.paidVal == 500 and result[0].despesa.paid == 0 and result[0].savedVal == 300, "val, paidVal, paid, savedVal must be 1800, 500, 0, 300"
        print(self.getJustifiedSuccessMsg("find"))

    def testUpdate(self):
        # find and update test row
        result = self.findTestRow()
        model = result[0]
        newVal = 1300
        newSavedVal = 200
        model.despesa.val = newVal
        model.savedVal = newSavedVal
        self.despesaAnualDAO.update(model)
        
        # find and validate updated test row
        result = self.findTestRow()
        model = result[0]
        print(model)
        assert model.despesa.val == newVal and model.savedVal == newSavedVal, "Val, SavedVal should be {}, {}".format(newVal, newSavedVal)
        print(self.getJustifiedSuccessMsg("update"))

    def testDelete(self):
        self.despesaAnualDAO.delete(self.findTestRow()[0])
        result = self.findTestRow()
        assert len(result) == 0, "there must be 0 DespesaAnual row"
        print(self.getJustifiedSuccessMsg("Delete"))

    def findTestRow(self):
        return self.despesaAnualDAO.find(self.getTestRowFilterModel())

    def getTestRowFilterModel(self):
        return DespesaAnual(despesa = Despesa(desc = 'desp test', month = '2018-02-01'))
