class Player:
    def __init__(self, name, stack, position, cards, bet):
        self.name = name
        self.stack = stack
        self.cards = cards
        self.position = position
        self.bet = bet





def main():
    p1 = Player(100)
    print(p1.stack)

main()
