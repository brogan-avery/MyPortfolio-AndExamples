"""
***************************************************
Title: Custom mapping/ lambda functions demo
Author: Brogan Avery
Created: 2020-09-05
Description :
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

"""
Definition of the built in map() function - according to RealPython.com:
  Python's map() is a built-in function that allows you to process and
  transform all the items in an iterable without using an explicit for loop,
  a technique commonly known as mapping. map() is useful when you need to apply
  a transformation function to each item in an iterable and transform them
  into a new iterable
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
