#!/usr/bin/python3

from test.utils.ArgParseTest import ArgParseTest
from test.processor.DespesaMensalProcessorTest import DespesaMensalProcessorTest
from models.DespesaAnual import DespesaAnual
from models.DespesaTemp import DespesaTemp
from models.DespesaMensal import DespesaMensal
from models.Renda import Renda
from models.CarneLeao import CarneLeao
from processor.MonthProcessor import MonthProcessor
from processor.DespesaAnualProcessor import DespesaAnualProcessor
from processor.DespesaTempProcessor import DespesaTempProcessor
from processor.DespesaMensalProcessor import DespesaMensalProcessor
from processor.RendaProcessor import RendaProcessor
from processor.CarneLeaoProcessor import CarneLeaoProcessor

def clearMonthData(month):
    despesaAnual = DespesaAnual()
    despesaAnualProcessor = DespesaAnualProcessor(month)
    for despesaAnual in despesaAnualProcessor.find():
        despesaAnualProcessor.delete(despesaAnual)

    despesaTemp = DespesaTemp()
    despesaTempProcessor = DespesaTempProcessor(month)
    for despesaTemp in despesaTempProcessor.find():
        despesaTempProcessor.delete(despesaTemp)

    despesaMensal = DespesaMensal()
    despesaMensalProcessor = DespesaMensalProcessor(month)
    for despesaMensal in despesaMensalProcessor.find():
        despesaMensalProcessor.delete(despesaMensal)

    renda = Renda()
    RendaProcessor(month).delete(renda)

    carneLeao = CarneLeao()
    CarneLeaoProcessor(month).delete(carneLeao)

    MonthProcessor(month.user, month = month).delete(month)

monthProcessor = MonthProcessor('Test', month = '01/9999')
months = monthProcessor.find()
month = None
if len(months) == 1:
    month = months[0]

if month:
    clearMonthData(month)
else:
    month = monthProcessor.month

print("\nTesting ArgParse\n")

ArgParseTest().test()

print("\nTesting DespesaMensalProcessor\n")

DespesaMensalProcessorTest(month).test()
