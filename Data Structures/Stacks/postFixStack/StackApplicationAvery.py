
"""
***************************************************************
* Title: infix to postfix
* Author: Brogan Avery
* Created : 2021-02-14
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: macOS Catalina
* IDE: PyCharm
* Copyright : This is my own original work  based on specifications issued by the course instructor
* Description : An app that converts infix to postfix notation and uses stacks
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
***************************************************************
"""

def convert(infixEq):
    stack = [] # stack to hold the operators
    convertedToPostFix = [] # to put operands into

    for i in range(len(infixEq)):
        if infixEq[i].isalnum(): # boolean to see if its is a number or letter ( same as a more time consuming loop of selecting the i if it was in the alphabet or a num of 0-9)
            convertedToPostFix.append(infixEq[i]) # add the numbers and letters to the list of what will become the postfix notation of the infix equation

        # the next to elifs handle parentheses

        elif infixEq[i] == '(':
            stack.append(infixEq[i])

        elif infixEq[i] == ')':
            while True:
                top = stack.pop() #uses a temp holder to juggle around values
                if top == '(':
                    break
                elif top.isalnum() == False:
                    convertedToPostFix.append(top)
        else:
            if stack: # if the stack is not empty, it uses the following to set order of precedence
                top = stack[-1]
                p1 = 0
                p2 = 0

                if top == "-":
                    p1 = 1
                if top == "+":
                    p1 = 2
                if top == "/":
                    p1 = 3
                if top == "*":
                    p1 = 4
                if top == "^":
                    p1 = 5

                if infixEq[i] == "-":
                    p2 = 1
                if infixEq[i] == "+":
                    p2 = 2
                if infixEq[i] == "/":
                    p2 = 3
                if infixEq[i] == "*":
                    p2 = 4
                if infixEq[i] == "^":
                    p2 = 5

                while stack and p1 >= p2 and infixEq[i].isalnum() == False:
                    convertedToPostFix.append(stack.pop())
                    if len(stack) > 0:
                        top = stack[-1]
            stack.append(infixEq[i])

    while stack:
        convertedToPostFix.append(stack.pop())

    return convertedToPostFix # returns a list of the characters that compose the equation written in postfix

# MAIN--------------------------------------------------------------------
if __name__ == '__main__':

    inFixEq1 = "2+3*4"
    inFixEq2 = "a*b+5"
    inFixEq3 = "(1+2)*7"
    inFixEq4 = "a*b/c"
    inFixEq5 = "(a/(b-c+d))*(e-a)*c"
    inFixEq6 = "a/b-c+d*e-a*c"
    inFixEq7 = input("Enter an infix notation equation to convert")

    print(convert(inFixEq1))
    print(convert(inFixEq2))
    print(convert(inFixEq3))
    print(convert(inFixEq4))
    print(convert(inFixEq5))
    print(convert(inFixEq6))
    print(convert(inFixEq7))