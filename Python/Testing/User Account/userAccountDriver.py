'''
Author: Brogan Avery
Date: 2020/09/01
Project Title: Driver for user account class
'''

from userAccount import *
#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
# assuming that these are new accounts
    account1 = UserAccount('Joan Evens', 'checking')
    account1.deposit(400)
    account1.withdraw(250)
    print(account1.display())

    print('\n')

    account2 = UserAccount('Bill Waters', 'Savings')
    account2.deposit(50)
    account2.withdraw(100)
    print(account2.display())
