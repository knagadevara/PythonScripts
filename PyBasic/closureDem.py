## closure demo
## Python sees that there is eference of variable x being called from inside the innner() function.
## Any variables created in the inner functions or outer functions will exist only till the runtime execution of the function.
## Unlike the 'closure variables' which creates a 'cell' to store the memory address of the object, its data type and its value.
## It will be a persistant block even after the eexecution is over, but the referencing and values remain.
import sys
def outer():
    x = 'Karthik'
    print('Hex id of x is: {0} '.format(hex(id(x))))
    def inner():
        print('My name is {0}'.format(x))
        print('Hex id of x is: {0} '.format(hex(id(x))))
    print('Hex id of inner is: {0} '.format(hex(id(inner))))
    return inner

print('Hex id of outer is: {0} '.format(hex(id(outer))))
outer()
ex = outer()
print('Hex id of ex is: {0} '.format(hex(id(ex))))
ex()
print(sys.getrefcount(ex) - 1)
print(sys.getrefcount(outer) - 1)
print(ex is outer)
print(ex.__closure__)