## The main aim is to reduce the number of arguments when calling the function.
## Aim to calculate the distance of the codrdinates nearest to the origin and sort them.
from functools import partial

origin = (0,0)
coordinates = [(9,1) , (4,1) , (5,8) , (3,9) , (2,4) , (-4,1) , (-1,-5)]

## Formula to calculate the distance to origin
dist2O = lambda a,b: (a[0] - b[0])**2 + (a[1] - b[1])**2
## The limitation is calling the function is it will stop at the first iteration
# print(dist2O(coordinates, origin)) # TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
print(dist2O((1,1),origin)) # it takes 2 equal tuples

## To over come this in an easy way we can default one of the argument using partial
## which takes function and functions first positional parameters as arguments.
disFP = partial(dist2O, origin)
disFP((1,1))

## Now we can use sorted find the shortest cordinates
print(sorted(coordinates , key=disFP))
print(list(map(disFP, coordinates)))