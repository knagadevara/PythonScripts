#!/usr/bin/python3.6
from random import randint
rock, paper, sissors = "rock" , "paper" , "sissors"

def hidde():
    for i in range(10):
        print("###!!!---!!!---!!!---!!!------!!!---!!!---!!!---!!!###")
        print("\n>>> Rock \n<<<"+" "+"\n>>> PaPer \n<<<"+" "+"\n>>> Sissors \n<<<")
        print("###!!!---!!!---!!!---!!!------!!!---!!!---!!!---!!!###")

p1 = input("Enter your choice rock or paper or sissors:   ").lower()
hidde()
choi = randint(0,2)
if choi == 0:
    p2 = rock
elif choi == 1:
    p2 = paper
else:
    p2 = sissors
print(f"Computer played:  {p2}")
#p2 = input("Enter Player 2 choice rock or paper or sissors:   ")


if (p1 == p2) :
    print("DRAW!!!")
elif (p1 == rock and p2 == sissors) or (p2 == paper and p1 == sissors) or (p1 == paper and p2 == rock):
    print("Player 1 Wins!!!")
elif (p2 == rock and p1 == sissors) or (p1 == paper and p2 == sissors) or (p2 == paper and p1 == rock):
    print("Player 2 Wins!!!")
else:
    print("Somethign is wrong")
