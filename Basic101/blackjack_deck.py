#!/usr/bin/python3.6

from blackjack_cards import *

class BJDeck:

    def __init__(self):

        suits    =     ("Hearts", "Diamonds", "Clubs","Spades")
        values   =     ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.deck = [BJCards(value, suit) for suit in suits for value in values]

            
d = BJDeck()
print(d.deck)
