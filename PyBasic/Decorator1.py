#!/usr/bin/python3.6
## passon a function as an argument to another function
## the main goal here is not to change the signature/defination 
## of the original function but to pass it on to another and modify there.

## Example 1
def func1(fn):
    def func2():
        return "Hello {}".format(fn())
    return func2

@func1
def func3(): return "Karthik"
## fun3 = func1(func3)

@func1
def func4(): return "Bharathi"
## func4 = func1(func4)

## Example 2

def verify_divide(fn):
    def wrapper_divide(a , b):
        print("Checking if the division works")
        if b == 0:
            print("Cannot devide by Zero")
        else:
            print("the answer is: {}".format(fn(a,b)))
    return wrapper_divide

@verify_divide
def divideme(x, y):
    return x/y

## Example 3

def capitalme(fn):
    def wrapper_capitalizeme(*args, **kwargs):
        return "Capatilized {}".format(fn(*args, **kwargs)).upper()
    return wrapper_capitalizeme

@capitalme
def capme(word):
    return "Hello {}".format(word)
@capitalme
def family(monm,dad,son):
    return "Hello {} {} {}".format(monm,dad,son)


##Example 4 Type enforcing through Decorators
