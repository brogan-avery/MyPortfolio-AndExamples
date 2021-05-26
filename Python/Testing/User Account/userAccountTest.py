import unittest
from userAccount import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.newAccount = UserAccount('Jenny Marx', 'Savings')
        self.otherNewAccount = UserAccount('Tim Green', 'checking')

    def tearDown(self):
        del self.newAccount
        del self.otherNewAccount

    def test_deposit(self):
        self.newAccount.deposit(400)
        self.assertEqual(self.newAccount.balance,400)

        self.otherNewAccount.deposit(50)
        self.assertEqual(self.otherNewAccount.balance, 50)

    def test_withdraw(self):
        self.newAccount.deposit(400)
        self.newAccount.withdraw(250)
        self.assertEqual(self.newAccount.balance, 150)

        self.otherNewAccount.deposit(50)
        self.otherNewAccount.withdraw(100)
        self.assertEqual(self.otherNewAccount.balance,50)



if __name__ == '__main__':
    unittest.main()
