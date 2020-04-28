#!/usr/bin/python3

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Tue Apr 28 18:33:57 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import subprocess
from sys import exit ## To give a Custom exit status to consume for a different program
## Thr old way is to call the command ## subprocess.call(['command','parameters']) ## ## subprocess.call(['ls' , '-al'])
## Output will be shown on the stdout prompt, Exit code will be saved to a variable
ex_code = subprocess.call(['ls' , '-al'])
if ex_code != 0:
    print('Could not execute it\n')
else:
    print('Thats a Success\n')

## New way of doing things, saving the output of the command into a variable
try:
    output = subprocess.check_output(['df' , '-hTi'], shell=True , stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as err:
    print('Wrong Command Given:\n{0}\n'.format(err))
    exit(1)
except FileNotFoundError as err:
    print('No File Found:\n{0}\n'.format(err))
    exit(2)
except OSError as err:
    print('Unable to determine and run the given command:\n{0}\n'.format(err))
    exit(3)
else:
    print('{0}\n'.format(output.decode("utf-8")))

### Output format has to be decoded into "utf-8", it converts the object from bytes to str
print(type(output))
print(type(output.decode("utf-8")))