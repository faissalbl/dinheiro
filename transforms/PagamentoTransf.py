from transforms.GenericTransform import GenericTransform
from models.Despesa import Despesa
from models.DespesaTemp import DespesaTemp
from models.Pagamento import Pagamento
from models.Month import Month

class PagamentoTransf(GenericTransform):
    
    def getModelType(self):
        return Pagamento

    def buildJoinedModels(self, model, row):
        despesa = Despesa(
            id = row['id'], 
            month = Month(
                id = row['month_id'],
                month = row['despesa_month']
            )

        )
        despesaTemp = DespesaTemp(despesa = despesa)
        model.despesaTemp = despesaTemp