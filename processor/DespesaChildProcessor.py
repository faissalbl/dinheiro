from processor.GenericProcessor import GenericProcessor
from models.Despesa import Despesa
from models.DespesaMensal import DespesaMensal

class DespesaChildProcessor(GenericProcessor):
    
    def pay(self, model):
        id = model.despesa.id
        paidVal = model.despesa.paidVal
        modelType = self.getModelType()
        models = self.getDAO().find(modelType(despesa = Despesa(id = id, month = self.month))) 

        if len(models) != 1:
            return

        model = models[0]
        if paidVal:
            model.despesa.paidVal += paidVal
            if model.despesa.paidVal >= model.despesa.val:
                model.despesa.paid = 1

            if model.despesa.paidVal > model.despesa.val:
                model.despesa.val = model.despesa.paidVal
        else:
            model.despesa.paid = 1
            model.despesa.paidVal = model.despesa.val

        self.getDAO().update(model)
