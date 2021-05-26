'''
Author: Brogan Avery
Date: 2020/08/31
Project Title: Gathering input
'''

def get_num_of_scores():
    try:
        numOfScores = int(input('How many scores do you have to enter?'))
        if (numOfScores < 1):
            return 'You may only enter in the keys 1-9. You must enter in a valid digit above 0.'
        return numOfScores
    except(TypeError, ValueError):
        return 'You may only enter in the keys 1-9. You must enter in a valid digit above 0.'

def get_next_score(prompt = "Enter score: "):
    try:
        nextScore = int(input(prompt))
        if (nextScore < 0):
            return 'You may only enter in the keys 0-9. You must enter in a valid digit 0 or above.'
        return nextScore
    except(TypeError, ValueError):
        return 'You may only enter in the keys 0-9. You must enter in a valid digit 0 or above.'

#—————————————————————----------------------------------------
if __name__ == '__main__':
    scores = []
    numOfScores = ''

    print('Follow the prompts to enter the scores you have.')

    while (type(numOfScores) != int):
        numOfScores = get_num_of_scores()
        if (type(numOfScores) != int):
            print(numOfScores)

    while (len(scores)+1 < numOfScores):
        nextScore = get_next_score()
        if (type(nextScore) != int):
            print(nextScore)
        else:
            scores.append(nextScore)

    while (len(scores) < numOfScores):
        nextScore = get_next_score('Enter your last score: ')
        if (type(nextScore) != int):
            print(nextScore)
        else:
            scores.append(nextScore)

    print('\nHere is your list of scores: ', scores)
    avg = sum(scores) / len(scores)
    print('This is the average of the scores in your list: ', round(avg,1))