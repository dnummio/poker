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
            currPlayer = player.Player(amount);
            self.players.append(currPlayer);


    def round(self):

        #deals out the hand
        for player in self.players:
            hand = self.deck(2);
            player.getCards(hand);

        actionOver = false;
        while not actionOver:
            getUserInput();



    def getUserInput(self, minBetAmount, maxBetAmount):

        action = ''
        actionList = ['CA','CH','R','F','E']
        raised = 0;
        
        #if previous action was a raise
        if (minBetAmount > 0):
            actionList.remove('CH')


        #continuous prompt input from user
        while True:
            try:
                action = str.upper(input("Player" + str(self.playerTurn) + " (Ch)eck (Ca)ll  (R)aise  (F)old or (E)xit game? "))
            except ValueError:
                print("Oops! That was no valid action. Accepted", actionList, ". Try again...")
            else:
                if action in actionList:
                    
                    #if raise
                    if action == 'R':
                        while True:
                            try:
                                raised = int(input("Raise Amount: "))
                            except ValueError:
                                print("Oops! That was no valid action. Try again....")
                            else:
                                if (raised > self.BB):
                                    break;
                                else:
                                    print("Oops! That was no valid action. Try again....")
                    break
                else:
                    print("Oops! That was no valid action. Accepted", actionList, ".Try again...")

        if action == 'CH':
            return 'Checked',0
        elif action == 'CA':
            return 'Called',minBetAmount
        elif action == 'R':
            return 'Raised',raised
        elif action == 'F':
            return 'Fold',0
        else:
            quit()



def main():
    game = Game(1,1,2,[100])
    game.getUserInput(10,100)

main()
