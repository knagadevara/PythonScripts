import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

uconst=-273
dconst=5526
a=[]
if n:
    for i in input().split():
        a = a.append(i)
        if i <= int(uconst) | i >= int(dconst):
            print('Value of n should be between -273 to 5526')
        else:
            srt = sorted(n)
            n = list(n)
            print(i[0])


##

