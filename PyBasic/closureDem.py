## closure demo
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