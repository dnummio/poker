import deck

def bestHand(hands):
    #hands is a set of cards of size 7

    values = [0]*15;
    suits = {0:[],1:[],2:[],3:[]}

    for card in hands:
        values[card.value] += 1
        suits[card.suit].append(card.value)


    print(values)
    print(suits)


    #---------checks number matches and straights-------------
    i=0
    longestStreak = [];
    highestLongestStreak = [];
    
    #highest number of same cards
    highest = max(values[0],values[1])
    secondHighest = min(values[0],values[1]);

    while (i < 15):
        
        if (values[i] != 0):
            
            #checks for straights
            longestStreak.append(i);

            #checks max/secondMax
            if (values[i] > highest):
                secondHighest = highest
                highest=values[i]
            elif (values[i] > secondHighest):
                secondHighest = values[i]
        else:
            if (len(longestStreak) >= len(highestLongestStreak)):
                highestLongestStreak = longestStreak;
            
            longestStreak = [];

        i+=1;


    print(highestLongestStreak)
    print(highest)
    print(secondHighest)


    #-----------checks flushes--------------
    maxSuited = [];
    maxSuitedLength = 0;
    for key,value in suits.items():
        if (len(value) > maxSuitedLength):
            maxSuited = value
            maxSuitedLength = len(value);

    print(maxSuited)


    #----------check hand rankings----------

    #straight flush
    if ((maxSuitedLength > 4) and (len(highestLongestStreak)>4) and (maxSuited.sort() == highestLongestStreak.sort())):
        return 8;

    if (highest == 4):
        return 7;

    if ((highest == 3) and (secondHighest >= 2)):
        return 6;

    if (maxSuitedLength > 4):
        return 5;

    if (len(highestLongestStreak)>4):
        return 4;

    if (highest == 3):
        return 3;

    if (highest == 2 and secondHighest == 2):
        return 2

    if (highest == 2):
        return 1

    if (highest == 1):
        return 0



def main():

    array = [0]*9
    d = deck.Deck()

    for i in range(0,99999):
        d.shuffle();
        hand = d.deal(5);
        array[bestHand(hand)] += 1

    print(array)
    

main();
