size = int(input("Rnter range: "))

# for num in range(1,size + 1):
#     if num == 4 or num == 13:
#         state = "UN-Lucky"
#     elif num % 2 == 1:
#         state = "ODD"
#     else:
#         state = "EVEN"
#     print(f"{num} is {state}")

num = 0

while num <= size :
    if num == 4 or num == 13:
        state = "UN-Lucky"
    elif num % 2 == 1:
        state = "ODD"
    else:
        state = "EVEN"
    print(f"{num} is {state}")
    num += 1