## using sequencing to understand it better of our custom reduce.
## redcer function combines the first element with next element on the list
## evaluates the function on them, saves the result into the variable.
## from now on it would take consider the value saved in the result variable 
## and starts to evaluate the function on it with second element.
from functools import reduce

lst = [1 ,5, 12 ,24, 6, 15]
glst = ['', 'Karthik' , 0 , 1 , None , True , False]
Tlst = [True , True , True]
Flst = [False , False , False]
TF = Tlst,Flst
max_value = lambda x,y: x if x > y else y

def p_reducer(fn, sequ):
    result = sequ[0]
    for x in sequ[1:]:
        result = fn(result, x)
    return result

print(p_reducer(max_value, lst) , reduce(max_value, lst))

# Mathametical builtin Reducer's
max(lst)
min(lst)
sum(lst)

# Boolean builtin Reducer's
any(glst)
any(Flst)
any(TF)
all(glst)
any(Tlst)
any(TF)