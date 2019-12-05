#!/usr/bin/python3.6
## passon a function as an argument to another function
## the main goal here is not to change the signature/defination 
## of the original function but to pass it on to another and modify there.

from functools import wraps

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


##Example 4: persisting the function metadata by using 'wraps' decorator
count1 = dict()
countToT = 0
def Counter_Func(funcu):
    count2 = 0
    @wraps(funcu)
    def countMe(*args: 'data type of the passed function arguments', **kwargs ) -> 'data type of the passed function':
        """
        This is a generic inner function which can take in *args and **kwargs
        """
        global count1 , countToT
        nonlocal count2
        count2 += 1
        count1[funcu.__name__] = count2
        countToT += 1
        print("The {0} has been called internally for {1}".format(funcu, count1[funcu.__name__]))
        print("Total Function Counts {0}".format(countToT))
        return funcu(*args , **kwargs)
    return countMe

@Counter_Func
def addMe(a: int,b: int = 1) -> int:
    """Simply adds two values"""
    return a + b
@Counter_Func
def mulMe(a: int,b: int = 1 , * , c) -> int:
    """Simply multiplies three values"""
    return a * b * c

print(addMe(10, 100))
print(addMe.__closure__)
help(addMe)
print(mulMe(10, c = 3))
print(mulMe.__closure__)
help(mulMe)