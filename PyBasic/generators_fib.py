#!/usr/bin/python3.6

## generate fibinachee number 1,1,2,3,5,8,13
## generator function returns a generator which is inturn an iterator
def fib_num(a):
    x = a
    i = 0
    k = 1
    while k < a:

        nxt = k + i
        i = k
        k = nxt
        yield(i)

coubter = fib_num(100)
def callmeloop():
    for fib in coubter:
        print(fib)

callmeloop()