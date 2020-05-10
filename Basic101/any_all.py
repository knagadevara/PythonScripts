#!/usr/bin/python3.6

## any() will return the value of a complete set of collection if any one of the item in it is true
## all() will return the value true only if all the items will be true for the confitional.
## In general python evaluates '' null/none 0 as boolean false values.

mylist = [ 0, 2 , 3 , 4 , 5 ]


print(all(mylist))
print(any(mylist))

