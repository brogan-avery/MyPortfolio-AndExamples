'''
Author: Brogan Avery
Date: 2020/09/11
Project Title: text scraping
'''

'''
NOTE: 
When I started doing this, 
I ran into one of the same problems I noticed last week 
when working with regex. Assuming that I will get all instances of a word
by simply adding a space on each side of the word in the string eliminates
insistence where the word I am looking for is part of another word. However, when 
using this method, it will not count words that are followed by punctuation marks 
(like at the end of a sentence) or if the word I am looking for starts the 
entire passage. Rather that use regex to search for
 each possibility ( ' old ' , 'old ' , ' old.' , ' old, ' , etc),
I looked into the NLTK a little bit more to see if there was a better way to 
go about this that would cover all possibilities.  
I think by tokenizing the words in the way I did, it helps to overcome some of the
limitations of regex.  
'''

from nltk.tokenize import sent_tokenize, word_tokenize

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
    print("___Moby Dick___")
# store file text to a string variable named text
    text = ''
    with open('Moby_Dick_Chapter_1.txt','r') as file:
        for line in file:
            text = text + line

# tokenize every word and punctuation mark treated as an individual token
    tokens_with_punc = word_tokenize(text)

# takes the list of tokenized words and removes the punctuation marks so they do not mess up the word count latter
    tokens = []
    for token in tokens_with_punc:
        if (token.isalnum()):
            tokens.append(token)

# get count of words that = old
    i = 0
    for token in tokens:
        if(token.lower() == 'old'):
            i = i + 1

    print('Number of times the word "old" appears in the chapter: ',i)

# get count of words that = water
    i = 0
    for token in tokens:
        if(token.lower() == 'water'):
            i = i + 1

    print('Number of times the word "water" appears in the chapter: ',i)

# tokenize every sentence
    sentences = sent_tokenize(text)

# get sentence count and word count to find average words in sentences
    numOfSentences = 0
    for sentence in sentences:
        numOfSentences = numOfSentences + 1

    numOfSentences = numOfSentences - 2 #to remove the chapter number and name which are conuted as sentences in the tokenization process

    wordCount = 0
    for token in tokens:
        wordCount = wordCount + 1

    avgWordCount = (wordCount/numOfSentences)

    print('The average number of words in a sentence in this chapter is: ', round(avgWordCount))

    print("___Sense and Sensibility___")
# store file text to a string variable named text
    text = ''
    with open('Sense_and_Sensibility_Chapter_1.txt','r') as file:
        for line in file:
            text = text + line

# tokenize every word and punctuation mark treated as an individual token
    tokens_with_punc = word_tokenize(text)

# takes the list of tokenized words and removes the punctuation marks so they do not mess up the word count latter
    tokens = []
    for token in tokens_with_punc:
        if (token.isalnum()):
            tokens.append(token)

# get count of words that = old
    i = 0
    for token in tokens:
        if(token.lower() == 'old'):
            i = i + 1

    print('Number of times the word "old" appears in the chapter: ',i)

# get count of words that = water
    i = 0
    for token in tokens:
        if(token.lower() == 'water'):
            i = i + 1

    print('Number of times the word "water" appears in the chapter: ',i)

# tokenize every sentence
    sentences = sent_tokenize(text)

# get sentence count and word count to find average words in sentences
    numOfSentences = 0
    for sentence in sentences:
        numOfSentences = numOfSentences + 1

    wordCount = 0
    for token in tokens:
        wordCount = wordCount + 1

    avgWordCount = (wordCount/numOfSentences)

    print('The average number of words in a sentence in this chapter is: ', round(avgWordCount))







