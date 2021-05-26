'''
Author: Brogan Avery
Date: 2020/09/01
Project Title: User account class
'''

class UserAccount:
    def __init__(self, accountName, type, balance = 0):
        self.accountName = accountName
        self.balance = balance
        self.type = type

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if (amount <= self.balance):
            self.balance = self.balance - amount
        else:
            print('Sorry, you are too low on funds.')

    def display(self):
        return 'Account Summery:\n' + 'Account holder: ' + str(self.accountName) + '\nAccount Type: ' + str(self.type) + '\nCurrent Balance: ' + str(self.balance)


