"""
***************************************************
Title: hourly employee basic functions
Author: Brogan Avery
Created: 2020-02-13
Description :
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

def hourly_employee_input():
    '''gets employee info from input here, then prints it here'''
    min_hours = 0
    max_hours =140
    min_pay = 7.25 #we assume at least....
    max_pay = 150 #a  cap on max hourly earning potential to hopfully limit accidental entries of crazy unlikely numbers
    valid_entry = False

    while (valid_entry == False ):
       name = input("Enter name: ")
       if (name.isalpha()):
           valid_entry = True
       else:
            print("Invaid entry, try again")

    valid_entry = False

    while (valid_entry == False ):
       try:
           hours = int(input("Enter hours worked: "))
           if (min_hours <= hours <= max_hours ):
               valid_entry = True
           else:
               print("Invaid entry, try again")
       except ValueError:
           print("Invaid entry, try again")

    valid_entry = False

    while (valid_entry == False):
       try:
           pay = float(input("Enter pay rate: "))
           if (min_pay <= pay <= max_pay):
               valid_entry = True
               print("-------------")
               print("NAME: " , name.capitalize())
               print("HOURS WORKED: ", hours)
               print("PAY RATE: $", pay)
           else:
                print("Invaid entry, try again")
       except ValueError:
            print("Invaid entry, try again")

#MAIN-----------------------
hourly_employee_input()
