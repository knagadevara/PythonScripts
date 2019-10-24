#!/usr/bin/python3
### takes in a function and a iterable
## iterable means  list tuple dictionary
## variable = map(function, iterable)
## function mostly one liner lambda

mylist = [ 2 , 3 , 4 , 5 ]
cube = list(map(lambda x: x*x*x , mylist))

print(cube)