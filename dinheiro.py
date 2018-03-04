#!/usr/bin/python3

import sys
import os

abspath = os.path.abspath(__file__)
dirpath, filename = os.path.split(abspath)

sys.path.append(dirpath)

from utils import argparser 
from models.Despesa import Despesa
from models.DespesaMensal import DespesaMensal
from models.DespesaAnual import DespesaAnual
from models.DespesaTemp import DespesaTemp
from processor.DespesaMensalProcessor import DespesaMensalProcessor
from processor.DespesaAnualProcessor import DespesaAnualProcessor
from processor.DespesaTempProcessor import DespesaTempProcessor
from processor.GenericProcessor import GenericProcessor

mon = GenericProcessor().month
mon = '{}/{}'.format(mon.month, mon.year)

def change_month(params = None):
    global mon 
    mon = params[0]

def ls_desp(params = None):
    despesas = DespesaMensalProcessor(mon = mon).ls()
    for d in despesas:
        print(d)

def add_desp(params = None):
    despesaMensal = DespesaMensal()
    despesaMensal.despesa.desc = input('Description: ')
    despesaMensal.despesa.val = input('Value: ')
    DespesaMensalProcessor(mon = mon).add(despesaMensal)

def rm_desp(params = None):
    despesaMensal = DespesaMensal(despesa = Despesa(id = params[0]))
    DespesaMensalProcessor(mon = mon).rm(despesaMensal)

def pay_desp(params = None):
    id = params[0]
    paidVal = None
    if len(params) > 1:
        paidVal = float(params[1])

    despesaMensal = DespesaMensal(despesa = Despesa(id = id, paidVal = paidVal))
    DespesaMensalProcessor(mon = mon).pay(despesaMensal)    

def ls_desp_an(params = None):
    despesas = DespesaAnualProcessor(mon = mon).ls()
    for d in despesas:
        print(d)

def add_desp_an(params = None):
    despesaAnual = DespesaAnual()
    despesaAnual.despesa.desc = input('Description: ')
    despesaAnual.despesa.val = input('Value: ')
    DespesaAnualProcessor(mon = mon).add(despesaAnual)

def rm_desp_an(params = None):
    despesaAnual = DespesaAnual(despesa = Despesa(id = params[0]))
    DespesaAnualProcessor(mon = mon).rm(despesaAnual)

def pay_desp_an(params = None):
    id = params[0]
    paidVal = None
    if len(params) > 1:
        paidVal = float(params[1])

    despesaAnual = DespesaAnual(despesa = Despesa(id = id, paidVal = paidVal))

    DespesaAnualProcessor(mon = mon).pay(despesaAnual)

def ls_desp_tmp(params = None):
    despesas = DespesaTempProcessor(mon = mon).ls()
    for d in despesas:
        print(d)
        for p in d.pagamentos:
            print('    ' + str(p))

        print()

def rm_desp_tmp(params = None):
    despesaTemp = DespesaTemp(despesa = Despesa(id = params[0]))
    DespesaTempProcessor(mon = mon).rm(despesaTemp)

def pay_desp_tmp(params = None):
    id = params[0]
    despesaTemp = DespesaTemp(despesa = Despesa(id = id))
    DespesaTempProcessor(mon = mon).pay(despesaTemp)

def add_desp_tmp(params = None):
    despesaTemp = DespesaTemp()
    despesaTemp.despesa.desc = input('Description: ')
    despesaTemp.despesa.val = input('Value: ')
    despesaTemp.months = int(input('Months: '))
    DespesaTempProcessor(mon = mon).add(despesaTemp)

methods = dict({
    'change_month': change_month,
    'ls_desp': ls_desp,
    'add_desp': add_desp,
    'rm_desp': rm_desp,
    'pay_desp': pay_desp,
    'ls_desp_an': ls_desp_an,
    'add_desp_an': add_desp_an,
    'rm_desp_an': rm_desp_an,
    'pay_desp_an': pay_desp_an,
    'ls_desp_tmp': ls_desp_tmp,
    'add_desp_tmp': add_desp_tmp,
    'rm_desp_tmp': rm_desp_tmp,
    'pay_desp_tmp': pay_desp_tmp
})

while True:
    args = input('dinheiro - month: {}> '.format(mon))
    if args == 'exit' or args == 'quit':
        sys.exit(0)

    args = args.split()

    # insert dummy because the argparser expects the first arg to be the program name
    args.insert(0, 'dummy')

    method_name = None
    param = None
    try:
        method_name, params = argparser.parseArgs(argv = args)
    #    print("method_name: {}, params: {}".format(method_name, params))
    except Exception as ex:
        print(ex)

    if (method_name):
        method = None

        if (method_name in methods.keys()):
            method = methods[method_name]

        if (method):
            if (params):
                method(params = params)
            else:
                method()
        else:
            print ("implement {}".format(method_name))

sys.exit(0)
