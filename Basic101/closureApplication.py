## Count how many time a function is run
count1 = dict()
countToT = 0
def Counter_Func(funcu):
    count2 = 0
    def countMe(*args, **kwargs):
        global count1 , countToT
        nonlocal count2
        count2 += 1
        count1[funcu.__name__] = count2
        countToT += 1
        print("The {0} has been called internally for {1}".format(funcu, count1[funcu.__name__]))
        print("Total Function Counts {0}".format(countToT))
        return funcu(*args , **kwargs)
    return countMe

def addMe(a,b):
    return a + b

def mulMe(a,b):
    return a * b

addFunv1 = Counter_Func(addMe)
addFunv2 = Counter_Func(addMe)
mulFunc1 = Counter_Func(mulMe)
print(addFunv1(21,1))
print(addFunv1(2,1)) ; print(addFunv2(1,1))
print(addFunv1(2,2))
print(mulFunc1(2,2))
print(mulFunc1(1,2))
print(addFunv2(5,1))
print(addFunv1(3,3))
print(addFunv1.__code__.co_freevars)
print(addFunv1.__closure__)
print(addFunv2.__code__.co_freevars)
print(addFunv2.__closure__)
print(mulFunc1.__code__.co_freevars)
print(mulFunc1.__closure__)