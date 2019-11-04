## Shared Closures, refer to the same parent object[variable] in the memory and if the base variable value changes, 
## so does the referencing dependant variable's everywhere unless they are singleton and immutable.
## Closure variables gets evaluated not until the function gets called, the reference always points to the same cell which further points to
## a memory location containing the value, That memory location[ inside the cell] will be updated to the result of the last function call evaluation.
def outer():
    x = 'Sai'
    y = 'Karthik'
    z = ''
    count = 0
    def inner1():
        nonlocal z
        nonlocal count
        z = 'Nagadevara'
        count += 1
        print('Full name: {0} {1}, Counter: {2}'.format(z,y, count))
    
    def inner2():
        nonlocal z
        nonlocal count
        z = 'Aravedhagan'
        count += 1
        print('Full name: {0} {1}, Counter: {2}'.format(z,y, count))
    
    return inner1 , inner2

fx1 , fx2 = outer()
print('Memory address of outer: {0}'.format(hex(id(outer()))))
print('Function of outer[which is inner1 functions][0]: {0}'.format(hex(id(outer()[0]))))
print('Function of outer[which is inner2 functions][1]: {0}'.format(hex(id(outer()[1]))))
print('fx1: {0}'.format(hex(id(fx1))))
print('fx1 being called: {0}'.format(hex(id(fx1()))))
print('fx2: {0}'.format(hex(id(fx2))))
print('fx2 being called: {0}'.format(hex(id(fx2()))))
print('Closure values in fx1: {0}'.format(fx1.__closure__))
print('Closure values in fx2: {0}'.format(fx2.__closure__))
fx1()
fx2()
print(fx1.__code__.co_freevars)
## Shared scopes example 2

def adder(n):
    def inner(x):
        return x + n
    return inner
add1 = adder(1) # sealing the value of n to 1
add2 = adder(2) # sealing the value of n to 2
add3 = adder(3) # sealing the value of n to 3
print('Closure values in add1: {0}'.format(add1.__closure__))
print('Closure values in add2: {0}'.format(add2.__closure__))
print('Closure values in add3: {0}'.format(add3.__closure__))
print('Closure values in add1 evaluation Value: {0} , Memory address Hexid: {1} , Evaluation HexId: {2}'.format(add1(10), hex(id(add1)),hex(id(add1(10)))))
print('Closure values in add2 evaluation Value: {0} , Memory address Hexid: {1} , Evaluation HexId: {2}'.format(add2(20), hex(id(add2)),hex(id(add2(20)))))
print('Closure values in add3 evaluation Value: {0} , Memory address Hexid: {1} , Evaluation HexId: {2}'.format(add3(30), hex(id(add3)),hex(id(add3(30)))))
print('Closure values in add1 evaluation Value: {0} , Memory address Hexid: {1} , Evaluation HexId: {2}'.format(add1(11), hex(id(add1)),hex(id(add1(11)))))
print('Closure values in add1 evaluation Value: {0} , Memory address Hexid: {1} , Evaluation HexId: {2}'.format(add1(11), hex(id(add1)),hex(id(add1(11)))))
# Closures can also be used in the loops and lambda's

def adder():
    a = []
    for n in range(1,10):
        a.append(lambda x, y=n: x + y)
    return a