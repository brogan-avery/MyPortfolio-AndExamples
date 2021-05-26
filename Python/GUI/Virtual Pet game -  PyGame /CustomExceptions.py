"""
Created on: Apr  25

@author: Brogan Avery

title: Custom Exceptions

desc: contains custom exceptions
"""

# raised if game window is closed by the X button
class WindowXOut(Exception):
    def __init__(self, message = None):
        if message == None:
           message = "You closed the game window before the game was done running. Program terminated."
           self.message = message
        super(WindowXOut,self).__init__(message)

# raised if cash variable is set bellow 0
class InDebt(Exception):
    def __init__(self, message = None):
        if message == None:
           message = "Something has gone wrong with the game and you have gone into debt!"
           self.message = message
        super(InDebt,self).__init__(message)