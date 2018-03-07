from dao.GenericDAO import GenericDAO
from dao.DespesaChildDAO import DespesaChildDAO
from transforms.DespesaMensalTransf import DespesaMensalTransf

class DespesaMensalDAO(DespesaChildDAO):

    # updates despesa
    def update(self, model):
        GenericDAO.update(self, model.despesa)


    def getTransform(self):
        return DespesaMensalTransf()

    def copyDespesasToMonth(self, model, month):
        query = self.getQuery(model, 'copy')
        self.executeUpdate(query, params = {'month': month})
