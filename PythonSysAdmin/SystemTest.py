#!/usr/bin/python3

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

        # By Author: knagadevara
        # Date: Tue Apr 28 11:57:27 IST 2020
        # Scripting Language: python
        # Copyright:: 2020, The Authors, All Rights Reserved.

#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#

# Read input from console and save in variable

def gatherInfo():
    ScptLang = str(input('Scripting Language [Python/Shell/Bash/Ruby]]  : ')).lower().strip()
    fileName = str(input('File Name [With no Extension]: ')).lower().strip()
    relVersn = str(input('Version Number: ')).strip()
    relTypeM = str(input('Release Type [Major or Minor]: ')).lower().strip()
    return (ScptLang, fileName, relVersn, relTypeM)

def TemplateContent(ScptLang, fileName, Versioning):
    print(ScptLang)
    print(fileName)
    print(Versioning)

while True:
    ScptLang, fileName, relVersn, relTypeM = gatherInfo()
    if relTypeM == 'major':
        Version = relVersn+'.'+'0'
        Content = TemplateContent(ScptLang, fileName, Versioning=Version)
        break
    elif relTypeM == 'minor':
        Version = '0'+'.'+relVersn
        Content = TemplateContent(ScptLang, fileName, Versioning=Version)
        break
    else:
        print('Failed to create a File!')

Content = "\n" + "#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#" + "\n" + "\n\t# By Author: " + "\n\t# Date:" + "\n\t# Scripting Language: " +  "\n\t# Copyright:: $, The Authors, All Rights Reserved. \n" + "\n" + "#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#" + "\n" + "\n"


### To Write to a file in a condition that the file exists

with open(fileName,'x') as ScrFl:
    ScrFl.write(Content)