class GenericTransform:
    
    
    def transform(self, result):
        cols, rows = result
        numCols = len(cols)
        modelType = self.getModelType()
        propertyToColumnDict = modelType().getPropertyToColumnDict()
        models = []
        for row in rows:
            model = modelType()
            for col in cols:
                if (col in propertyToColumnDict.keys()):
                    col = propertyToColumnDict[col]
                else:
                    col = None

                if (not col):
                    continue
                print(col)
                val = row[col]
                setattr(model, col, val)
            
            self.buildJoinedModels(model, row)
            models.append(model)

        return models
            

    def getModelType(self):
        raise NotImplementedError('this has not been implemented')

    #------------------------------------------------------------------------
    # Fetches the dependencies from row (example tipo_renda_id, desc) and sets in model
    # at the appropriate property (example tipoRenda)
    #------------------------------------------------------------------------
    def buildJoinedModels(self, model, row):
        raise NotImplementedError('this has not been implemented')