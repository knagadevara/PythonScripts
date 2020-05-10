#!/usr/bin/python3.6

# size = int(input("Rnter range: "))

# for num in range(1,size + 1):
#     if num == 4 or num == 13:
#         print(f"{num} UnLucky")
#     elif num % 2 == 1:
#         print(f"{num} is odd")
#     else:
#         print(f"{num} is even")

size = int(input("Rnter range: "))

for num in range(1,size + 1):
    if num == 4 or num == 13:
        state = "UN-Lucky"
    elif num % 2 == 1:
        state = "ODD"
    else:
        state = "EVEN"
    print(f"{num} is {state}")