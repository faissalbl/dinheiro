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
from processor.DespesaMensalProcessor import DespesaMensalProcessor
from processor.DespesaAnualProcessor import DespesaAnualProcessor

def ls_desp(params = None):
    despesas = DespesaMensalProcessor().ls()
    for d in despesas:
        print(d)

def add_desp(params = None):
    despesaMensal = DespesaMensal()
    despesaMensal.despesa.desc = input('Description: ')
    despesaMensal.despesa.val = input('Value: ')
    DespesaMensalProcessor().add(despesaMensal)

def rm_desp(params = None):
    despesaMensal = DespesaMensal(despesa = Despesa(id = params[0]))
    DespesaMensalProcessor().rm(despesaMensal)

def pay_desp(params = None):
    id = params[0]
    paidVal = None
    if len(params) > 1:
        paidVal = float(params[1])

    despesaMensal = DespesaMensal(despesa = Despesa(id = id, paidVal = paidVal))
    DespesaMensalProcessor().pay(despesaMensal)    

def ls_desp_an(params = None):
    despesas = DespesaAnualProcessor().ls()
    for d in despesas:
        print(d)

def add_desp_an(params = None):
    despesaAnual = DespesaAnual()
    despesaAnual.despesa.desc = input('Description: ')
    despesaAnual.despesa.val = input('Value: ')
    DespesaAnualProcessor().add(despesaAnual)

def rm_desp_an(params = None):
    despesaAnual = DespesaAnual(despesa = Despesa(id = params[0]))
    DespesaAnualProcessor().rm(despesaAnual)

def pay_desp_an(params = None):
    id = params[0]
    paidVal = None
    if len(params) > 1:
        paidVal = float(params[1])

    despesaAnual = DespesaAnual(despesa = Despesa(id = id, paidVal = paidVal))

    DespesaAnualProcessor().pay(despesaAnual)

def ls_desp_tmp(params = None):
    print('Listing despesas temporarias...')

methods = dict({
    'ls_desp': ls_desp,
    'add_desp': add_desp,
    'rm_desp': rm_desp,
    'pay_desp': pay_desp,
    'ls_desp_an': ls_desp_an,
    'add_desp_an': add_desp_an,
    'rm_desp_an': rm_desp_an,
    'pay_desp_an': pay_desp_an,
    'ls_desp_tmp': ls_desp_tmp
})

method_name = None
param = None
try:
    method_name, params = argparser.parseArgs()
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
