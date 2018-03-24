from processor.GenericProcessor import GenericProcessor
from processor.RendaProcessor import RendaProcessor
from models.Despesa import Despesa

class DespesaChildProcessor(GenericProcessor):
    
    def __init__(self, month = None):
        super().__init__(month = month)
        self.rendaProcessor = RendaProcessor(month = month)

    def pay(self, model):
        id = model.despesa.id
        paidVal = model.despesa.paidVal
        modelType = self.getModelType()
        modelFilter = modelType(despesa = Despesa(id = id))
        modelFilter.setMonth(self.month)
        models = self.getDAO().find(modelFilter) 

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

    def sum(self):
        modelType = self.getModelType()
        model = modelType()
        model.setMonth(self.month)
        resultModel = self.getDAO().sum(model)[0]
        return resultModel.despesa.val or 0

    def add(self, model):
        super().add(model)
        self.rendaProcessor.updateReserva()

    def delete(self, model):
        super().delete(model)
        self.rendaProcessor.updateReserva()

    def update(self, model):
        super().update(model)
        self.rendaProcessor.updateReserva()
