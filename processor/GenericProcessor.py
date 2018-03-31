class GenericProcessor:

    def __init__(self, month):
        self.month = month

    def getDAO(self):
        raise NotImplementedError('subclasses must implement this')

    def getModelType(self):
        raise NotImplementedError('this has not been implemented')

    def find(self):
        model = self.getModelType()()
        model.setMonth(self.month)
        return self.getDAO().find(model)

    def count(self):
        model = self.getModelType()()
        model.setMonth(self.month)
        return self.getDAO().count(model)

    def add(self, model):
        model.setMonth(self.month)
        self.getDAO().add(model)

    def delete(self, model):
        model.setMonth(self.month)
        self.getDAO().delete(model)

    def update(self, model):
        model.setMonth(self.month)
        self.getDAO().update(model)

    def copy(self):
        model = self.getModelType()()
        model.setMonth(self.month)
        self.getDAO().copy(model)

