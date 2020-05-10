#!/usr/bin/python3.6


## creating my custome ietrable and ietrator

name  = 'Karthik'
phone = [9,7,0,0,5,5,6,6,7,7]

def my_forloop(ietrable, cfunc):
    
    itx = iter(ietrable)

    while True:

        try:
            gx =  next(itx)
        except StopIteration:
             break
        else:
            cfunc(int(gx))


def addme(x):
    x += x
    print(x)

print(my_forloop(phone, addme))