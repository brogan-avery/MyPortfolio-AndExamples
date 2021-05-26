'''
Author: Brogan Avery
Date: 2020/09/01
Project Title: decorator demo
'''

def myDecorator(myFunction):
    def inner_function():
        myFunction()
        myFunction()
    return inner_function

@myDecorator
def myFunction():
    print('something')

#——————————————————————————————————————————————————
if __name__ == '__main__':
    myFunction()
