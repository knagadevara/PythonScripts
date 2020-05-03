#!/usr/bin/python3

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Sun May  3 23:05:01 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

from json import dump, dumps, load, loads
from random import random, randint, randrange, uniform, choice
from os import getenv, getenvb
path='/usr/share/dict/words'
count = int(getenv("FILE_COUNT") or "100")
words = [word for word in open(path, 'r').readlines()]

for i in range(1 , count+1):
    r_data = { "amount" : round(uniform(1750.00,2500.00),3), "miword" : choice(words) }
    try:
        with open('/tmp/created/jsonFile{0}.json'.format(i), 'w') as f:
            dump(r_data, f)
    except Exception as err:
        print(err)
    else:
        print('Successfully created {0} number of files'.format(count))