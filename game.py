import player
import deck


class Game:
    def __init__(self, numPlayers, smallBlind, bigBlind, buyIns):

        self.players = []
        self.numberPlayers = numPlayers
        self.SB = smallBlind
        self.BB = bigBlind
        self.deck = deck.Deck();
        self.pot = 0;
        
        #determines which player is the small blind
        self.SBpos = 1;

        #denotes which player is up to play. This is initialized to the UTG
        self.playerTurn = (self.SBpos+2)%2;
        
        for amount in buyIns:
            currPlayer = player.humanPlayer(amount);
            self.players.append(currPlayer);


    def round(self):

        #deals out the hand
        for player in self.players:
            hand = self.deck(2);
            player.getCards(hand);

        playersLeft = numPlayers;
        while (playersLeft > 0):
            Action, amount = getUserInput();

            playersLeft = playersLeft - 1;


def main():
    game = Game(1,1,2,[100])
    game.players[0].getMove(10,100,game.BB);

main()
