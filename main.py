import random

thisdeck={              #dictonary of deck of cards
"Ace of Spade": 11,
"2 of Spade": 2,
"3 of Spade": 3,
"4 of Spade": 4,
"5 of Spade": 5,
"6 of Spade": 6,
"7 of Spade": 7,
"8 of Spade": 8,
"9 of Spade": 9,
"10 of Spade": 10,
"Jack of Spade": 10,
"Queen of Spade": 10,
"King of Spade": 10,

"Ace of Clubs": 11,
"2 of Clubs": 2,
"3 of Clubs": 3,
"4 of Clubs": 4,
"5 of Clubs": 5,
"6 of Clubs": 6,
"7 of Clubs": 7,
"8 of Clubs": 8,
"9 of Clubs": 9,
"10 of Clubs": 10,
"Jack of Clubs": 10,
"Queen of Clubs": 10,
"King of Clubs": 10,

"Ace of Hearts": 11,
"2 of Hearts": 2,
"3 of Hearts": 3,
"4 of Hearts": 4,
"5 of Hearts": 5,
"6 of Hearts": 6,
"7 of Hearts": 7,
"8 of Hearts": 8,
"9 of Hearts": 9,
"10 of Hearts": 10,
"Jack of Hearts": 10,
"Queen of Hearts": 10,
"King of Hearts": 10,

"Ace of Diamonds": 11,
"2 of Diamonds": 2,
"3 of Diamonds": 3,
"4 of Diamonds": 4,
"5 of Diamonds": 5,
"6 of Diamonds": 6,
"7 of Diamonds": 7,
"8 of Diamonds": 8,
"9 of Diamonds": 9,
"10 of Diamonds": 10,
"Jack of Diamonds": 10,
"Queen of Diamonds": 10,
"King of Diamonds": 10
}

print('\n\n')

listOfDeckKeys= list(thisdeck.keys())           # creating list of keys from dictonary
listOfDeckValues=list(thisdeck.values())        # creating list of values

playerOneListOfKeys=[]              # declaration of empty list for player 1 and 2
playerOneListOfValues=[]
playerTwoListOfKeys=[]
playerTwoListOfValues=[]

random.shuffle(listOfDeckKeys)      # shuffling deck

userInput='Y'                       # variable to run the 1st while loop

value1=0                            
value2=0

while userInput=='Y' or userInput=='y':         # 1st loop to run if user wants to play again when asked the question at the end
    
    while True:             # loop to run until total card value of a player is 21
        rand1=random.randint(0,51)              # random number to get a card from deck
        cardPlayer1=listOfDeckKeys[rand1]       # get a random key from deck list
        playerOneListOfKeys.append(cardPlayer1)         # get the key and value into the 1st player list
        playerOneListOfValues.append(thisdeck.get(cardPlayer1))

        print('Player one was dealt: ',cardPlayer1)

        if (11 in playerOneListOfValues) and (sum(playerOneListOfValues) >21):   # checking if Ace should be counted as 1 or 11
            z1=playerOneListOfValues.index(11)          # find the index of 11
            playerOneListOfValues.pop(z1)               # pop 11 from list
            playerOneListOfValues.append(1)             # add 1 to the list
            value1=sum(playerOneListOfValues)           # sum the values
        else:
            value1=sum(playerOneListOfValues)


        rand2=random.randint(0,51)              # random number to get a card from deck
        cardPlayer2=listOfDeckKeys[rand2]       # get a random key from deck list
        playerTwoListOfKeys.append(cardPlayer2)              # get the key and value into the 2nd player list
        playerTwoListOfValues.append(thisdeck.get(cardPlayer2))

        print('Player Two was dealt: ',cardPlayer2)

        if (11 in playerTwoListOfValues) and (sum(playerTwoListOfValues) >21):    # checking if Ace should be counted as 1 or 11
            z2=playerTwoListOfValues.index(11)          # find the index of 11
            playerTwoListOfValues.pop(z2)               # pop 11 from list
            playerTwoListOfValues.append(1)             # add 1 to the list
            value2=sum(playerTwoListOfValues)           # sum the values
        else:
            value2=sum(playerTwoListOfValues)

        print('\n')

        if(value1>=21):         # breaking the loop if any player total exceeds 21
            break
        elif (value2>=21):
            break


    print("Player One Points: ",value1)         # showing player total
    print("Player Two Points: ",value2)

     # conditions of when players win
    if (value1==value2 and (not(11 in playerTwoListOfValues or 1 in playerTwoListOfValues)) and (not(11 in playerOneListOfValues or 1 in playerOneListOfValues))):
        print('\nGame is Draw!!')
    elif (value1==value2 and (11 in playerTwoListOfValues or 1 in playerTwoListOfValues) and (not(11 in playerOneListOfValues or 1 in playerOneListOfValues))):
        print('\nPlayer 2 Wins!!')
    elif (value1==value2 and (not(11 in playerTwoListOfValues or 1 in playerTwoListOfValues)) and (11 in playerOneListOfValues or 1 in playerOneListOfValues)):
        print('\nPlayer 1 Wins!!')
    elif (value2==21):                
        print('\nPlayer 2 Wins!!')
    elif (value1==21):
        print('\nPlayer 1 Wins!!')
    elif(value1>value2 and value2<=21):
        print('\nPlayer 2 Wins!!')
    elif(value1<value2 and value1<=21):
        print('\nPlayer 1 Wins!!')
    elif(value1>21 and value2>21):
        print('\nBoth player exceed 21!!')
        
    
    playerOneListOfKeys.clear()             # clearing lists for player 1 and 2
    playerOneListOfValues.clear()
    playerTwoListOfKeys.clear()
    playerTwoListOfValues.clear()   

    userInput=input('\n\nDo You Want To Play Another Round? (Y/N): ') # asking user if they wants to play again.
    
print('\nGAME ENDED!!')
print('\n\n')
