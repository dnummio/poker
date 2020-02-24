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
        self.SBpos = 0;

        #denotes which player is up to play. This is initialized to the UTG
        self.playerTurn = (SBpos+2)%2;
        
        for amount in buyIns:
            currPlayer = player.Player(amount);
            players.append(currPlayer);


    def round(self):

        #deals out the hand
        for player in players:
            hand = self.deck(2);
            player.getCards(hand);

        actionOver = false;
        while not actionOver:
            getUserInput();



    def getUserInput(self):

        action = ''
        actionList = ['C','R','F','E']


        #continuous prompt input from user
        while True:
            try:
                action = str.upper(input("Player " + str(self.playerTurn) + "(C)heck  (R)aise  (F)old or (E)xit game ?"))
            except ValueError:
                print "Oops! That was no valid action. Accepted", action_list, ". Try again..."
            else:
                if action in action_list:
                    break
                else:
                    print "Oops! That was no valid action. Accepted", action_list, ".Try again..."

        if action == 'C':
            return 'Checked'
        elif action == 'R':
            return 'Raised'
        elif action == 'F':
            return 'Fold'
        else:
            quit()
