## To use a global variable if any ambigious variableas are there
## we have to use the 'global' keyword before the variable name
a = 11
def OuterFunc():
    #global a
    #print('Global Inside Outer, a: '.format(a))
    a = 22
    print('Re-Assigned Outer Layer of Function, a: {}'.format(a))
    def InnerFunc1():
        #nonlocal a
        #print('Non-Local Inside Inner, a: '.format(a))
        a = 33
        print('Re-Assigned Inner 1 Layer of Function, a: {}'.format(a))
        def InnerFunc2():
            nonlocal a
            a = 44
            print('Non-Local Inside Inner 2 Layer, a: '.format(a))
        return InnerFunc2()
    return InnerFunc1()
    print('Calling the Variable in Outer, a: '.format(a))

print('Calling the Variable Globally, a: '.format(a))
OuterFunc()
print('Calling the Variable Globally after re-assignment, a: '.format(a))