from test.GenericTest import GenericTest
from dao.RendaDAO import RendaDAO
from models.Renda import Renda
from models.TipoRenda import TipoRenda

class RendaDAOTest(GenericTest):

    rendaDAO = RendaDAO()

    def test(self):
        self.testAdd()
        self.testFind()
        self.testUpdate()
        self.testDelete()

    def testAdd(self):
        renda = Renda(tipoRenda = TipoRenda(id = 'reserva'), val = 1800, month = '2018-02-01')
        self.rendaDAO.add(renda)
        print(self.getJustifiedSuccessMsg('add'))

    def testFind(self):
        result = self.findTestRow()
        assert len(result) == 1, "there must be 1 Renda row"
        assert type(result[0]).__name__ == 'Renda', "Result type must be Renda"
        assert result[0].tipoRenda.desc == 'Reserva Financeira', "Resulting row must have a Tipo Renda 'Reserva Financeira'"
        print(self.getJustifiedSuccessMsg("find"))

    def testUpdate(self):
        # find and update test row
        result = self.findTestRow()
        model = result[0]
        newVal = 7200
        model.val = newVal
        self.rendaDAO.update(model)
        
        # find and validate updated test row
        result = self.findTestRow()
        model = result[0]
        print(model)
        assert model.val == newVal, "Val should be {}, and not {}".format(newVal, model.val)
        print(self.getJustifiedSuccessMsg("update"))

    def testDelete(self):
        self.rendaDAO.delete(self.getTestRowFilterModel())
        result = self.findTestRow()
        assert len(result) == 0, "there must be 0 Renda row"
        print(self.getJustifiedSuccessMsg("Delete"))

    def findTestRow(self):
        return self.rendaDAO.find(self.getTestRowFilterModel())

    def getTestRowFilterModel(self):
        return Renda(tipoRenda = TipoRenda(id = 'reserva'), month = '2018-02-01')
