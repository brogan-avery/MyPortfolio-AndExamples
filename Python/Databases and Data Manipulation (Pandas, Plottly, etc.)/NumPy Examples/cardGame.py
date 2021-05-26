'''
Author: Brogan Avery
Date: 2020/09/17
Project Title: Card Game with numpy arrays
'''

from numpy import *

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
#create card deck array
    cardDeck = arange(1,37)
# shuffle the cards
    random.shuffle(cardDeck)
# pass the cards out to the players
    playersHands = cardDeck.reshape(6,6)
# create identity array, multiply it by players hands
    identityArray = identity(6)

    identityArray = multiply(identityArray,playersHands)
    identityArray = negative(identityArray)

# made the two arrays flat to merge the negative numbers back in
    i = 0
    playersHands = playersHands.flatten()
    identityArray = identityArray.flatten()
    while(i < identityArray.size):
        if(identityArray[i] != 0):
            playersHands[i] = identityArray[i]
        i = i + 1

# reshaping the data back to 6 x 6
    playersHands = playersHands.reshape(6, 6)

# create an array that contains each of the players scores
    playerScores = arange(6)
    i = 0
    for row in playersHands:
        playerScores[i] = row.sum()
        i = i + 1

# print results
    print('Here are the results of the game: ')

    i = 1
    for score in playerScores:
        print('Player ',i , ': ', score)
        i = i + 1

    print('The winner is: Player ',argmax(playerScores) + 1, ' with a score of: ', max(playerScores) )
