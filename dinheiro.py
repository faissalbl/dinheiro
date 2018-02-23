#!/usr/bin/python3

import sys
import os

abspath = os.path.abspath(__file__)
dirpath, filename = os.path.split(abspath)

sys.path.append(dirpath)

from utils import argparser 

def ls_desp():
    print('Listing despesas...')

def ls_desp_an():
    print('Listing despesas anuais...')

def ls_desp_tmp():
    print('Listing despesas temporarias...')

methods = dict({
    'ls_desp' : ls_desp,
    'ls_desp_an' : ls_desp_an,
    'ls_desp_tmp' : ls_desp_tmp
})

method_name = None
param = None
try:
    method_name, param = argparser.parseArgs()
    print("method_name: {}, param: {}".format(method_name, param))
except Exception as ex:
    print(ex)

if (method_name):
    method = None

    if (method_name in methods.keys()):
        method = methods[method_name]

    if (method):
        if (param):
            method(param)
        else:
            method()
    else:
        print ("implement {}".format(method_name))

sys.exit(0)
