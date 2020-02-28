import card
from random import shuffle


class Deck:
    def __init__(self):

        #tells you which cards are left in the deck
        self.cards = []

        #tells you the cards that are in play
        self.inplay = []

        #initializes deck of cards
        for suit in range(0,4):
            for value in range (2,15):
                self.cards.append( card.Card(value, suit) )


    #resets and shuffles the deck
    def shuffle(self):
        self.cards.extend(self.inplay)
        self.inplay= []
        shuffle(self.cards)


    #deals a specified number of cards
    def deal(self, numCards):
        
        if (numCards > len(self.cards)):
            return False

        inplay = []
        for i in range(0,numCards):
            currCard = self.cards.pop(0)
            inplay.append(currCard)

        self.inplay.extend(inplay);
        return inplay

    def cardsLeft(self):
        return len(self.cards)

    def getInplay(self):
        return self.inplay;
