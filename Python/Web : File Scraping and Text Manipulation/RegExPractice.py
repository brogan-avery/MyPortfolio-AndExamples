'''
Author: Brogan Avery
Date: 2020/09/05
Project Title: RegEx demo
'''

import re
#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
    passage = 'I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.'

# f count in passage
    fList = re.findall('f', passage,flags=re.IGNORECASE)

    i = 0
    for f in fList:
        i = i + 1

    print('The letter "f"/"F" is found', i, 'times in the passage.')

# count words that start with f
    wordTokens = re.split("\s", passage)

    i = 0
    for word in wordTokens:
        startsWithFList = re.findall('^f', word, flags=re.IGNORECASE)
        if startsWithFList:
            i = i + 1

    print(i, 'words in the passage start with "f"/"F".')

# count the number of times the word 'not' is in passage
    i = 0
    for word in wordTokens:
        isNot = re.findall('^not$', word, flags=re.IGNORECASE)
        if isNot:
            i = i + 1

    print(i, 'word in the passage is the word "not".')

# changing words in the passage

    changedPassage = re.sub('I ', ' You ', passage)
    changedPassage = re.sub(' my ', ' your ', changedPassage)
    changedPassage = re.sub(' me | me. ', ' you ', changedPassage)

    print(changedPassage)


