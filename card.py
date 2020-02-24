class Card:
    def __init__(self, value, suit):
        self.value= value
        self.suit = suit

    def __str__(self):
        text = ""

        #2-10 are just the string representations of the value
        if self.value == 11:
            text = "J"
        elif self.value == 12:
            text = "Q"
        elif self.value == 13:
            text = "K"
        elif self.value == 14:
            text = "A"
        else:
            text = str(self.value)

        #deals with the suits of the cards

        if self.suit == 0:    #D-Diamonds
            text += "/D" 
        elif self.suit == 1:  #H-Hearts
            text += "/H"
        elif self.suit == 2:  #S-Spade
            text += "/S"
        else:                   #C-Clubs
            text += "/C" 
            
        return text 


