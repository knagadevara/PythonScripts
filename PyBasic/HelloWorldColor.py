#!/usr/bin/python3.6

from pyfiglet import *
from termcolor import colored


mylist = ['red' , 'green' , 'yellow' , 'blue' , 'magenta' , 'cyan',  'white']
miput = str(input('Please enter the text: '))
f = Figlet(font='slant', direction='auto', width=100)
fig = f.renderText(miput)

while True:
    ciput = str(input('Which color do you want(red, green, yellow, blue, magenta, cyan, white): ')).lower()  
    if ciput in mylist:
        break
    else:
        continue
    
bgc = str(input('Do you want Back Ground? [yes/no]: ')).lower()
bklist = ['on_red', 'on_green', 'on_yellow', 'on_blue', 'on_magenta' , 'on_cyan' , 'on_white']
while True:
    if bgc == 'yes':
        choc = str(input('Choose the color on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white: '))
        if choc in bklist:
            break
    elif bgc == 'no':
        choc = 'on_blue'
        break
    else:
        choc = str(input('Please try again: '))
        continue

print(colored(fig , ciput , choc))