#!/usr/bin/python3.6

from random import choice

class BJCards:

    def __init__(self, value , suit):
        self.value   =  value
        self.suit    =  suit

    def __repr__(self):
        return "{0} of {1}".format(choice(self.value) , choice(self.suit))