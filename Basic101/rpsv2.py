#!/usr/bin/python3.6
from random import randint
rock, paper, sissors = "rock" , "paper" , "sissors"

def hidde():
    print("###!!!---!!!---!!!---!!!------!!!---!!!---!!!---!!!###")
    print("\n>>> Rock \n<<<"+" "+"\n>>> PaPer \n<<<"+" "+"\n>>> Sissors \n<<<")
    print("###!!!---!!!---!!!---!!!------!!!---!!!---!!!---!!!###")

#win_count  = 2
game_count = 0
player1 = 0
player2 = 0

while player1 < 2 and player2 < 2 :
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
        player1 += 1
        player2 += 0
    elif (p2 == rock and p1 == sissors) or (p1 == paper and p2 == sissors) or (p2 == paper and p1 == rock):
        print("Player 2 Wins!!!")
        player1 += 0
        player2 += 1
    else:
        print("Something is wrong")
    #game_count += 1
    print(f"Score Board \nPlayer 1: {player1}\nPlayer 2: {player2}")

if  player1 == player2:
    print(f"Series Draw")
elif player2 > player1:
    print(f"Player 2 wins the series with {player2} points")
else:
    print(f"Player 1 wins the series with {player1} points")
