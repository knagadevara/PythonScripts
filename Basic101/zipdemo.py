## Zip function takes in more than 1 iterable then combines elements one-on-one.
## it returns a zip generator object which is a tuple.

l1 = [1,2,3,4,5]
l2 = [9,8,7,6]
l3 = [5,1,4]
l4 = ['a' , 'b' , 'c' , 'd']
l5 = ['z' , 'y' , 'x']

zp = zip(l1,l2,l3)
xp = zip(l1,l4,l5,l2)
print(zp , xp)

for x in zp:
    print(x)
for x in xp:
    print(x)
