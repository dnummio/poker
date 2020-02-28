import card

class Player:
    def __init__(self,stack,number):
        self.number = number;
        self.stack = stack;
        self.cards = [];

    def getNumber(self):
        return self.number
    
    def getCards(self, cardsDealt):
        for card in range(0, len(cardsDealt)):
            self.cards.append(card);

    def returnCards(self):
        return self.cards

    def takeFromStack(self,chips):
        self.stack = self.stack - chips;
    
    def getStack(self):
        return self.stack

    #default is fold
    def getMove(self, minBetAmount, maxBetAmount, BB):
        return 'Fold',0

#------------------------BAD PLAYER------------------------------------
class noojPlayer(Player):
    def __init__(self, stack,number):
        super().__init__(stack,number);

    def getMove(self, minBetAmount, maxBetAmount, BB):
        if (minBetAmount > 0):
            return 'Call', minBetAmount
        else:
            return 'Check',0


#------------------------HUMAN PLAYER------------------------------------
class humanPlayer(Player):
    
    #calls constructor of parent class
    def __init__(self, stack,number):
        super().__init__(stack,number);


    #user input for move
    def getMove(self, minBetAmount, maxBetAmount, BB):
        action = ''
        actionList = ['CA','CH','R','F','E']
        
        #determines amount that was raised
        raised = 0;

        #if previous action was a raise                                                                              
        if (minBetAmount > 0):
            actionList.remove('CH')


        #continuous prompt input from user                                                                           
        while True:
            try:
                action = str.upper(input("Player" +str(self.number)+": (Ch)eck (Ca)ll  (R)aise  (F)old or (E)x\
it game? "))
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
                                if (raised > BB):

                                    #case all in
                                    if (raised > maxBetAmount):
                                        raised = maxBetAmount;
                                    break;
                                else:
                                    print("Oops! That was no valid action. Try again....")
                    break
                else:
                    print("Oops! That was no valid action. Accepted", actionList, ".Try again...")

        if action == 'CH':
            return 'Check',0
        elif action == 'CA':
            return 'Call',minBetAmount
        elif action == 'R':
            return 'Raise',raised
        elif action == 'F':
            return 'Fold',0
        else:
            quit()
    

