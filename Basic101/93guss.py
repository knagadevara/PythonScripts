#!/usr/bin/python3.6

from random import randint

gues = randint(1,10)
#print(f"{gues}")
troya = True

while troya :
    my_gues = int(input("Guess it: "))
   # while my_gues != gues:
    if my_gues > gues :
        print("Greater\n")
    elif my_gues < gues:
        print("Lower\n")
    else:
        print("Correct\n")
        answer = input("Want to play Again?[y/n] ")
        if answer == "y":
            gues = randint(1,10)
        else:
            print("Thank you for Playing\n\U0001f600")
            troya = False