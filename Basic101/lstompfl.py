from random import *
#rang_num = [x for x in ]
# rand_jok = randint(1,10)
# print(rand_jok)

## filter function will go through the iterable and finds out the truthiness of it by testing it with the given function.
# List comprenhenssion (<expression> for <var> in <iterable> [if <condition>])
l = 2,3,4,5
m = 6,7,8,9

# Finding Square root with loop
sq = []
for i in l:
    sq.append(i**2)
print(sq)

#finding square root with function and map
mpsq = map(lambda sq: sq**2 , l)
print(mpsq)
print(list(mpsq))

# list comprehenssion way
x = [e**2 for e in l]
print(x)

mp = map(lambda x,y: x+y, l,m)
print(list(mp))
## as map and filter are higher order functions and return a map/filter type ieterable object, which needs to be converted to a list
# What is Zip
# zp = zip(l,m)
# print(list(zp))
# list comprehenssion way using the fnctionality of zip
addme = [x+y for x,y in zip(l,m)]
print(addme)

## converting a filter function to list comprehenssion

fil = list(filter(lambda s: s%2 == 0 , l))
print(fil)

liff = [x for x in l if x%2==0]
print(liff)

## combining lit and filter
mpfil = list(filter(lambda z: z < 100 ,map(lambda x: x**6, l)))
print(mpfil)

### Expressing it simply through list compren
limpfil = [x**6 for x in l if x**6 < 100]
print(limpfil)