#!/usr/bin/python3

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Tue Apr 28 21:07:51 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

from argparse import ArgumentParser
from sys import exit

describeMe = ' %{prog}s will be used to search the file for a giben word '
serHelp = ' %{prog}s -s <Search Term>'
filHelp = ' %{prog}s -f <Search Term>'

parseme = ArgumentParser(prog='searchFile' , description=describeMe)
parseme.add_argument('--snippet','-s', help=serHelp , required=True , type=str)
parseme.add_argument('--fileName' , '-f' , help=filHelp, required=True)
parsed_args = parseme.parse_args()
matched = []
ser_snip = parsed_args.snippet.lower()

try:
    filName = open(parsed_args.fileName , 'r')
except FileNotFoundError as err:
    print(err)
    exit(1)
else:
    with filName:
        try:
            lines = filName.readlines()
        except PermissionError as err:
            print(err)
            exit(2)
        except OSError as err:
            print(err)
            exit(3)
        else:
            for word in lines:
                if ser_snip in word:
                    matched.append(word)
finally:
    print(matched)

### Can also be done using List Comprenhension
print([word for word in lines if ser_snip in word.lower()])