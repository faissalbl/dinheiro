from dao.DespesaChildDAO import DespesaChildDAO
from dao.PagamentoDAO import PagamentoDAO
from transforms.DespesaTempTransf import DespesaTempTransf
from models.Pagamento import Pagamento

class DespesaTempDAO(DespesaChildDAO):

    pDAO = PagamentoDAO()

    # find despesas temp and load pagamentos
    def find(self, model):
        despesasTemp = super().find(model)
        for despesaTemp in despesasTemp:
            pagamentos = self.pDAO.find(Pagamento(despesaTemp = despesaTemp))
            despesaTemp.pagamentos = pagamentos

        return despesasTemp

    # adds despesa temp and pagamentos
    def add(self, model):
        despesaId = super().add(model)
        for pagamento in model.pagamentos:
            pagamento.despesaTemp.despesa.id = despesaId
            self.pDAO.add(pagamento)

        return despesaId

    # updates despesa temp and pagamentos
    def update(self, model):
        super().update(model)
        for pagamento in model.pagamentos:
            self.pDAO.update(pagamento)

    # delete pagamentos and despesa temp
    def delete(self, model):
        self.pDAO.delete(Pagamento(despesaTemp = model))
        super().delete(model)

    def getTransform(self):
        return DespesaTempTransf()
