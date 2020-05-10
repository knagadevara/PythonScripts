#!/usr/bin/python3.6

# def even_numbers(a , b):
#     x = [ x for x in range(a,b) if x % 2 == 0 ]
#     return x

# print(even_numbers(10,40))

# def evenorood(a , b):
#     x = ["Even" if x % 2 == 0 else "Odd" for x in range(a,b)]
#     return x

# print(evenorood(10,20))

def dic_even_odd(a , b):
    q = { x:("Even" if x % 2 == 0 else "Odd") for x in [y for y in range(a , b)] }
    return q

print(dic_even_odd(10 , 20))
