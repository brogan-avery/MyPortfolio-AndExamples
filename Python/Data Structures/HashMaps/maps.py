"""
***************************************************************
* Title: Hash Map/ Table
* Author: Brogan Avery
* Created : 2021-04-13
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that demonstrates the creation of hash tables by using email and name key, value pairs
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""
from hashMap import HashMap

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':

    hashTable = HashMap() # map/table object

    #vals
    hashTable.insertPair('jsnow@gmail.com', 'Jonny Snow')
    hashTable.insertPair('nrogers@example.com', 'Nigel Rogers')
    hashTable.insertPair('psmith@example.com', 'Pam Smith')
    hashTable.insertPair('twest@example.com', 'Tanya West')
    print(hashTable,"\n")

    #search
    print(hashTable.search('jsnow@gmail.com'),"\n")
    print(hashTable.search('badEmail'), "\n")

    #has key or not
    print(hashTable.hasKey('nrogers@example.com'),"\n")
    print(hashTable.hasKey('badEmail'),"\n")

    # delete
    hashTable.delete('twest@example.com')
    print(hashTable)