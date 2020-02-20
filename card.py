class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

def main():
    c1 = Card("A", "H")
    print(c1.face)

main()
