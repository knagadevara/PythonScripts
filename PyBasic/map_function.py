#!/usr/bin/python3
### takes in function, iterable and returns a generator object. 
## iterable means  list tuple dictionary
## variable = map(function, iterable)
## function mostly one liner lambda
## an map object will be empty if it is called off once

mylist = [ 2 , 3 , 4 , 5 ]

cube = map(lambda x: x*x*x , mylist)
print(cube)

xi=[]
for x in cube:
    xi.append(x)
print(xi)

yi=[]
for y in cube:
    yi.append(y)
print(yi)

## as the cube object is iterated and stored in xi it becomes empty.
## cannot use contents of map object cube again in 'yi'. 