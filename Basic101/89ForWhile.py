#!/usr/bin/python3.6

i = 0
size = int(input("Rnter range: "))
# for i in range(size,0,-1):
#     print("\U0001f600"*i)

# while i <= size:
#     print("\U0001f600"*i)
#     i += 1

while i < size:
    cpunt = 1
    smil = "\U0001f600"
    while cpunt < i:
        smil += "\U0001f600"
        cpunt += 1
    i += 1

# i = 1
#
#
#
#