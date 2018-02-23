from test.GenericTest import GenericTest
from dao.TipoRendaDAO import TipoRendaDAO
from models.TipoRenda import TipoRenda

class TipoRendaDAOTest(GenericTest):

    tipoRendaDAO = TipoRendaDAO()

    def test(self):
        self.testFind()

    def testFind(self):
        result = self.tipoRendaDAO.find(TipoRenda())
        assert len(result) == 6, "there must be 6 TipoRenda rows"
        assert type(result[0]).__name__ == 'TipoRenda'
        print("first row: {}".format(result[0]))
        print(self.getJustifiedSuccessMsg("find"))
