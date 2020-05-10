#!/usr/bin/python3

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Sun May  3 23:05:01 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

from json import dump
from random import uniform, choice
from os import getenv, makedirs

logger={}

path = r'/usr/share/dict/words'
created_path = r'/tmp/created'

try:
    makedirs(created_path, mode=0o755, exist_ok=True)
except Exception as err:
    logger['fileError {0}'.format(created_path)] = err

count = int(getenv("FILE_COUNT") or "100")
words = [word.strip() for word in open(path, 'r').readlines()]

for i in range(1 , count+1):
    r_data = { "amount" : round(uniform(1750.00,2500.00),3), "miword" : choice(words) }
    try:
        with open("{0}/receipt_{1}.json".format(created_path,i), 'w') as f:
            dump(r_data, f)
    except Exception as err:
        logger['receiptFileErro{0}'.format(i)] = err
    else:
        print('Successfully created receipt{0}.json'.format(i))

print(logger)