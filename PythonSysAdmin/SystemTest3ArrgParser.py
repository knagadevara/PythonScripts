#!/usr/bin/python3

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Tue Apr 28 16:33:23 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

import argparse

## Helpful Content to display
argDesc='Creates a template with given scripting language extension'
gen1="Request you to provide the below as arguments for the file:" + \
        "\n %(prog)s python <name of file> \n \t for PYTHON... \n" + \
        "\n %(prog)s bash <name of file> \n \t for BASH...\n" + \
        "\n %(prog)s ruby <name of file> \n \t for RUBY...\n"
epilog="And that's how you'd run a the script"

### Initialization of Parser
parseme = argparse.ArgumentParser(prog='ArgumentParserTest' ,  description=argDesc, usage=gen1 , epilog=epilog )
parseme.add_argument('--fileName', '-f', type=str, help='Give a Valid filename without any special characters', required=True)
parseme.add_argument('--sLang', '-s', type=str, help='Give a Valid Scripting Language without any special characters')
parseme.add_argument('--appVersion', '-v', action='version', version='%(prog)s 1.0')
parseme.add_argument('--fLimit', '-l', type=int, help='Give a Valid Number')

## Saving the contents into a variable
arguments =  parseme.parse_args()
print(type(arguments))

with open(arguments.fileName, 'r') as rf1:
    readln = rf1.readlines()
    readln.reverse()

    if arguments.fLimit:
        readln = readln[:arguments.fLimit]

    for line in readln:
        print(line.strip()[::-1])