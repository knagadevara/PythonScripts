#!/usr/bin/python3.6

from random import choice

class Cards:

    
    suit    =     ("Hearts", "Diamonds", "Clubs","Spades")
    value   =     ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    def __repr__(self):
        return "{0} of {1}".format(choice(Cards.value) , choice(Cards.suit))