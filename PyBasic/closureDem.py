## closure demo
## Python sees that there is eference of variable x being called from inside the innner() function.
## Any variables created in the inner functions or outer functions will exist only till the runtime execution of the function.
## Unlike the 'closure variables' which creates a 'cell' to store the memory address of the object, its data type and its value.
## It will be a persistant block even after the eexecution is over, but the referencing and values remains.
## Here the 'outer function' is returning the memory address on its 'inner function' which is further being saved in to a variable 'ex' variable.
## Hence when we call 'ex()' it would get the outer variable 'x' which is a string with the help of cell referencing.
## Immutable data types[int,str] and singleton objects always point to the same memory location if the variable is kept unchanged.
import sys
def outer():
    x = 'Karthik'
    count = 0
    print('Hex id of x: {0} and count: {1}'.format(hex(id(x)), hex(id(count))))
    def inner():
        nonlocal count 
        count += 1
        print('Hex id of x: {0} and count: {1}'.format(hex(id(x)), hex(id(count))))
        return 'Name: {0} and Count: {1}'.format(x , count)
    print('Hex id of inner is: {0} '.format(hex(id(inner))))
    return inner

ex = fx = outer()
ex1 = outer()
## TO check all the free variables in the function and general reference validation
## print(ex.__code__._freevars)
print('Hex id of outer is: {0} '.format(hex(id(outer))))
outer()
print('Hex id of ex is: {0} '.format(hex(id(ex))))
print('What is in outer : {0} '.format(outer))
print('What is in ex : {0} '.format(ex))
print(sys.getrefcount(ex) - 1)
print(sys.getrefcount(outer) - 1)
a= ex is outer
b= ex is fx
c =ex is ex1
print('Are the memory references same? for ex is outer {0}, ex is fx {1}, ex is ex1 {2}'.format(a,b,c))
print('Closure values in ex: {0}'.format(ex.__closure__))
print('Closure values in fx: {0}'.format(fx.__closure__))
print('Closure values in ex1: {0}'.format(ex1.__closure__))
print('Values in ex: {0}'.format(ex()))
print('Values in ex: {0}'.format(ex()))
print('Values in fx: {0}'.format(fx()))
print('Values in fx: {0}'.format(fx()))
print('Values in ex1: {0}'.format(ex1()))
print('Values in ex1: {0}'.format(ex1()))
print('Values in ex: {0}'.format(ex()))