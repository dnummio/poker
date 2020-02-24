import card

class Player:
    def __init__(self, stack):
        self.stack = stack;
        


    self.cards = [];
    
    def getCards(self, cardsDealt):
        for card in range(0, len(cardsDealt)):
            self.cards.append(card);
