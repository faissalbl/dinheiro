from dao.GenericDAO import GenericDAO
from transforms.MonthTransf import MonthTransf

class MonthDAO(GenericDAO):

    def getTransform(self):
        return MonthTransf()
