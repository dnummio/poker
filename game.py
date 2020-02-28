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
        self.playerTurn = (self.SBpos+2) % self.numberPlayers;
        
        #denotes number of players that have folded
        self.numFolded = 0;

        #initialize array of Players
        number = 1;
        for amount in buyIns:
            currPlayer = player.humanPlayer(amount,number);
            self.players.append(currPlayer);
            number += 1




    
    def bettingRound(self, playersInHand, firstToAct, minBet):
        
        #players = array of players
        players = playersInHand;

        #index counter
        currPlayerIndex = firstToAct;

        #holds last bet size
        minBetAmount = minBet;

        #determines when action is over, is reset when raised
        playersLeftToAct = len(players);



        while(True):
            if players[currPlayerIndex] != None:
                maxBetAmount = players[currPlayerIndex].stack
                action, chips = players[currPlayerIndex].getMove(minBetAmount, maxBetAmount, self.BB)
            
#take chips from players and add to pot
                players[currPlayerIndex].takeFromStack(chips);
                self.pot += chips;

            #special conditions
                if (action == 'Fold'):
                    players[currPlayerIndex] = None;
                    self.numFolded += 1;
                

                elif (action == 'Raised'):
                
                #reopens the pot at raised amount
                    playersLeftToAct = len(players);
                    minBetAmount = chips;

            
            #increment counters 
            playersLeftToAct -= 1;
            currPlayerIndex = (currPlayerIndex+1)%len(players);


            #do while condition check
            if (self.numFolded  == self.numberPlayers - 1 or playersLeftToAct == 0):
                return players            




    #one round of hands
    def round(self):

        #deals out the hand
        for player in self.players:
            hand = self.deck.deal(2);
            player.getCards(hand);

        playersRemaining = self.players
        roundsRemaining = 3;

        #collects blinds
        playersRemaining[self.SBpos].takeFromStack(self.SB);
        playersRemaining[(self.SBpos+1) % self.numberPlayers].takeFromStack(self.BB);

        self.pot += (self.SB + self.BB);



        #3 rounds of betting
        while (roundsRemaining > 0):
            minBetAmount = 0;
            
            #preflop
            if (roundsRemaining == 3):
                minBetAmount = self.BB
            else:
                self.playerTurn = self.SBpos


            playersRemaining = self.bettingRound(playersRemaining, self.playerTurn, minBetAmount);

            #checks if winner found
            if (self.numFolded  == self.numberPlayers - 1):
                break;

            roundsRemaining -= 1;


        #showdown
        hands = []
        for player in playersRemaining:
            if player != None:
                playerCards = player.returnCards();
                cards = playerCards.extend(self.deck.getInplay());
                hands.append(cards);
            
        



            
        


def main():
    game = Game(2,1,2,[100,100])
    game.round()
    

main()
