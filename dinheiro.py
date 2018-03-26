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
from models.Pagamento import Pagamento
from models.Renda import Renda
from models.TipoRenda import TipoRenda
from processor.DespesaMensalProcessor import DespesaMensalProcessor
from processor.DespesaAnualProcessor import DespesaAnualProcessor
from processor.DespesaTempProcessor import DespesaTempProcessor
from processor.GenericProcessor import GenericProcessor
from processor.RendaProcessor import RendaProcessor
from processor.TipoRendaProcessor import TipoRendaProcessor
from processor.MonthProcessor import MonthProcessor

def change_month(params = None):
    global month 
    month = params[0]
    MonthProcessor.changeMonth(month)
    

def ls_desp(params = None):
    despesas = DespesaMensalProcessor(month = month).find()
    despesaMensalHeader = DespesaMensal()
    print(despesaMensalHeader.defOutputStrHeader())
    print(despesaMensalHeader.defOutputHr())
    for d in despesas:
        print(d.defOutputStr())

    print()

def add_desp(params = None):
    despesaMensal = DespesaMensal()
    despesaMensal.despesa.desc = input('Description: ')
    despesaMensal.despesa.val = input('Value: ')
    DespesaMensalProcessor(month = month).add(despesaMensal)

def rm_desp(params = None):
    despesaMensal = DespesaMensal(despesa = Despesa(id = params[0]))
    DespesaMensalProcessor(month = month).delete(despesaMensal)

def pay_desp(params = None):
    id = params[0]
    paidVal = None
    if len(params) > 1:
        paidVal = float(params[1])

    despesaMensal = DespesaMensal(despesa = Despesa(id = id, paidVal = paidVal))
    DespesaMensalProcessor(month = month).pay(despesaMensal)    

def ls_desp_an(params = None):
    despesas = DespesaAnualProcessor(month = month).find()
    despesaAnualHeader = DespesaAnual()
    print(despesaAnualHeader.defOutputStrHeader())
    print(despesaAnualHeader.defOutputHr())
    for d in despesas:
        print(d.defOutputStr())

    print()

def add_desp_an(params = None):
    despesaAnual = DespesaAnual()
    despesaAnual.despesa.desc = input('Description: ')
    despesaAnual.despesa.val = input('Value: ')
    DespesaAnualProcessor(month = month).add(despesaAnual)

def rm_desp_an(params = None):
    despesaAnual = DespesaAnual(despesa = Despesa(id = params[0]))
    DespesaAnualProcessor(month = month).delete(despesaAnual)

def pay_desp_an(params = None):
    id = params[0]
    paidVal = None
    if len(params) > 1:
        paidVal = float(params[1])

    despesaAnual = DespesaAnual(despesa = Despesa(id = id, paidVal = paidVal))

    DespesaAnualProcessor(month = month).pay(despesaAnual)

def ls_desp_tmp(params = None):
    despesas = DespesaTempProcessor(month = month).find()
    despesaTempHeader = DespesaTemp()
    pagamentoHeader = Pagamento()
    pagamentoHeadingSpace = '    '
    print(despesaTempHeader.defOutputStrHeader())
    print(despesaTempHeader.defOutputHr())
    for d in despesas:
        print(d.defOutputStr())
        print()

        print(pagamentoHeadingSpace + pagamentoHeader.defOutputStrHeader())
        print(pagamentoHeadingSpace + pagamentoHeader.defOutputHr())
        for p in d.pagamentos:
            print(pagamentoHeadingSpace + str(p.defOutputStr()))

        print()

def rm_desp_tmp(params = None):
    despesaTemp = DespesaTemp(despesa = Despesa(id = params[0]))
    DespesaTempProcessor(month = month).delete(despesaTemp)

def pay_desp_tmp(params = None):
    id = params[0]
    despesaTemp = DespesaTemp(despesa = Despesa(id = id))
    DespesaTempProcessor(month = month).pay(despesaTemp)

def add_desp_tmp(params = None):
    despesaTemp = DespesaTemp()
    despesaTemp.despesa.desc = input('Description: ')
    despesaTemp.despesa.val = input('Value: ')
    despesaTemp.months = int(input('Months: '))
    DespesaTempProcessor(month = month).add(despesaTemp)

def ls_renda(params = None):
    rendas = RendaProcessor(month = month).find()
    rendaHeader = Renda()
    print(rendaHeader.defOutputStrHeader())
    print(rendaHeader.defOutputHr())
    for r in rendas:
        print(r.defOutputStr())

    print()

def add_renda(params = None):
    rendaProcessor = RendaProcessor(month = month)
    tipoRenda = inputTipoRenda()
    renda = Renda(tipoRenda = tipoRenda)
    renda.val = input('Value: ')
    renda.taxable = inputTaxable()
    rendaProcessor.add(renda)

def inputTipoRenda():
    tiposRenda = TipoRendaProcessor().find()
    # rebuild list without the auto calculated ones
    tiposRenda = [x for x in tiposRenda if not x.auto]
    tipoRenda = None
    while True:
        print('Tipos Renda: ')
        nbr = 1
        for tr in tiposRenda:
            print('{}) {}'.format(nbr, tr.desc))
            nbr += 1

        tr_nbr = input('Tipo Renda: ')
        tr_nbr = int(tr_nbr) - 1
        if (tr_nbr >= 0 and tr_nbr < len(tiposRenda)):
            tipoRenda = tiposRenda[tr_nbr]
            break

        print()

    return tipoRenda

def inputTaxable():
    mTaxable = {'S': 1, 'N' : 0}
    while True:
        taxable = input('Tributavel? (S/N)')
        if taxable:
            taxable = mTaxable[taxable.upper()]
            return taxable


def rm_renda(params = None):
    renda = Renda(tipoRenda = TipoRenda(id = params[0]))
    RendaProcessor(month = month).delete(renda)

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
    'pay_desp_tmp': pay_desp_tmp,
    'ls_renda': ls_renda,
    'add_renda': add_renda,
    'rm_renda': rm_renda
})

month = GenericProcessor().month
month = '{}/{}'.format(month.month, month.year)
change_month(params = [month])

while True:
    args = input('dinheiro - month: {}> '.format(month))
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
