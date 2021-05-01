"""
***************************************************************
* Class Name: Hash Map
* Author: Brogan Avery
* Created: 2021-04-13
***************************************************************
"""

class HashMap:

    def __init__(self, size = 1000):
        self.size = size # max size
        self.hashTable = self.createPairBuckets()

    def createPairBuckets(self):
        return [[] for i in range(self.size)] # creates array for the pairs

    def insertPair(self, key, val):
        hashKey = hash(key) % self.size # Get the index from the key using hash function
        pairBucket = self.hashTable[hashKey] # Get the pairBucket corresponding to index
        foundKey = False # found or not
        for i, pair in enumerate(pairBucket):
            existingKey, existingVal = pair
            if existingKey == key: # check if the pairBucket has same key as the key to be inserted
                foundKey = True
                break
        if foundKey:# update or add pair
            pairBucket[i] = (key, val)
        else:
            pairBucket.append((key, val))

    def hasKey(self, key):
        hashKey = hash(key) % self.size  # Get the index from the key using hash function
        pairBucket = self.hashTable[hashKey]  # Get the pairBucket corresponding to index
        foundKey = False  # found or not
        for i, lookingFor in enumerate(pairBucket):
            existingKey, existingVal = lookingFor
            if existingKey == key:  # check if the pairBucket has same key as the key being searched
                foundKey = True
        return foundKey

    def search(self, key): # search by key
        hashKey = hash(key) % self.size # Get the index from the key using hash function
        pairBucket = self.hashTable[hashKey] # Get the pairBucket corresponding to index
        foundKey = False # found or not
        for i, lookingFor in enumerate(pairBucket):
            existingKey, existingVal = lookingFor
            if existingKey == key:  # check if the pairBucket has same key as the key being searched
                foundKey = True
                break
        if foundKey: # returns value or not found message
            return existingVal
        else:
            return "Not found"

    def delete(self, key): # delete pair by key
        hashKey = hash(key) % self.size  # Get the index from the key using hash function
        pairBucket = self.hashTable[hashKey]  # Get the pairBucket corresponding to index
        foundKey = False  # found or not
        for i, lookingFor in enumerate(pairBucket):
            existingKey, existingVal = lookingFor
            if existingKey == key:  # check if the pairBucket has same key as the key being searched
                foundKey = True
                break
        if foundKey:
            pairBucket.pop(i) # removes the pair if it exists
        return

    def hash(key, max):
        h = 0
        for i in range(len(key)):
            h = (h + ord(key[i]) * (max - 1)) % max
        return h

    def __str__(self):
        return "".join(str(i) for i in self.hashTable)


