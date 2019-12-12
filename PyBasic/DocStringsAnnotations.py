import inspect

for param in inspect.signature(divmod).parameters.values():
    print('{0}: {1}'.format(param.name, param.kind))
# def myFunc(a: 'Integer type only'  = 1 , b: 'Integer type only' = 1) -> 'Integer Object':
#     """This is the Documentation of the function myFunc()"""
#     pass

# print(myFunc.__doc__)
# #help(myFunc)
# print(myFunc.__annotations__)
import random
l = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]

ex = lambda x: random.random()

print(ex(l))


