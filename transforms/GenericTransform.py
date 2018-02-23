class GenericTransform:
    
    
    def transform(self, result):
        cols, rows = result
        numCols = len(cols)
        modelType = self.getModelType()
        columnToPropertyDict = modelType().getColumnToPropertyDict()
        models = []
        for row in rows:
            model = modelType()
            for col in cols:
                prop = None
                if (col in columnToPropertyDict.keys()):
                    prop = columnToPropertyDict[col]

                if (not prop):
                    continue

                val = row[col]
                setattr(model, prop, val)

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