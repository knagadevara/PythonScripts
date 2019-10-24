#!/usr/bin/python3.6

from KarthikCards import Cards
from random import shuffle

class Deck:

    def __init__(self):
        self.myDeck()

    def myDeck(self):
        ## this method should generate the 52 cards with all the unique possiblities.
        self.myDeckL = []
        self.decksize = 0
        while self.decksize < 52:
            i = Cards()
            x = str(i)
            if x in self.myDeckL:
                continue
            else:
                self.myDeckL.append(x)
                self.decksize += 1
        return sorted(self.myDeckL)
    
    def count(self):
        # tells how many cards we are left in Deck
        #self.counter =  self.myDeckL.__len__
        return int(len(self.myDeckL))
        #return self.counter

    def __repr__(self):
        # displays the cards in Deck
        return self.myDeckL

    def _deal(self, hdeal):
        
        #self.hdeal = int(input("Please let us know Howmany cards to be removed: "))     
        nocard = self.count()
        self.hdeal = hdeal
        actual = min([nocard , self.hdeal])
        if nocard == 0:
            raise ValueError("there are no cards left")
        rmdcards = self.myDeckL[-actual:]
        self.myDeckL = self.myDeckL[:-actual]
        return rmdcards

    def shuffleme(self):
        nocard = self.count()

        if nocard < 52:
            raise ValueError("There are only {0} cards in the Deck!! Cannot Shuffle".format(self.count()))
        else:
            shuffle(self.myDeckL)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, numr):
        return self._deal(numr)

# d = Deck()
# d._deal()
# d.shuffleme()