#!/usr/bin/python3

## filter will use a conditional function as a first argument and an iterable for the second argument
## the function supplied to filter() should return a boolean value and it will be checked against the 
## supplied list to it.

## filter(boolien_checker, iterable_list)

## filter <-- boolean-Check <-- list

mynum = [2 , 3 , 4, 6 ,7 ,8 ,9 , 11 ,12 ]
fil_test = filter(lambda x: x % 3 == 0 , mynum )

mylist = ['Karthi' , 'nagadevara' , 'steve' , 'ganga' , 'Hanuman']

def bool_check(x):
    val=[]
    for a in x:
        if len(a) <= 5:
            val.append(a)
    return val

xvar = map(lambda sg: "I am the instructor {0}".format(sg) , filter(lambda x : len(x) <= 5 , mylist ))

#tes = ["I am an Instructor {0}".format(m) for m in mylist if len(m) <= 5 ]
#print(tes)
print(list(xvar))

## using None in filter
print(list(filter(None, ['', 'Karthik' , 0 , 1 , None , True , False] )))