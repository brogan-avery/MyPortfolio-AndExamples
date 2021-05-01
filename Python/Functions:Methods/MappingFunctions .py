"""
***************************************************
Title: Mapping functions demo
Author: Brogan Avery
Created: 2020-09-05
Description :
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

def get_word_length(word):
    wordLength = len(word)
    wordInfo = [word,wordLength]
    return wordInfo
#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
    words = ['dog', 'horse', 'whale', 'pig', 'mouse', 'rabbit', 'deer', 'frog', 'gazelle', 'octopus', 'cat', 'fox', 'zebra', 'goat']
    result = map(get_word_length,words)
    wordsAndWordLengths = list(result)

    print(wordsAndWordLengths)

    for word in wordsAndWordLengths:
        print(word[1])
