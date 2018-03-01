#!/bin/bash

./01_argparse_test.py  
if [ $? -ne 0 ]; then
    exit 1
fi

./02_tipo_renda_dao_test.py  
if [ $? -ne 0 ]; then
    exit 1
fi

./03_renda_dao_test.py
if [ $? -ne 0 ]; then
    exit 1
fi

./04_despesa_mensal_dao_test.py
if [ $? -ne 0 ]; then
    exit 1
fi

./05_despesa_anual_dao_test.py
if [ $? -ne 0 ]; then
    exit 1
fi

./06_despesa_temp_dao_test.py
if [ $? -ne 0 ]; then
    exit 1
fi

./07_pagamento_dao_test.py
if [ $? -ne 0 ]; then
    exit 1
fi

echo "Test complete. All passed \o/ \o/ \o/"

exit 0
