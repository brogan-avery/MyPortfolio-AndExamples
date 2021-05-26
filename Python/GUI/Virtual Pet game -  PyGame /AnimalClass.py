
"""
Created on: Apr  1 2020

@author: Brogan Avery 

title: animal class

desc: animal class is super class and contains methods for pet actions, etc.
"""

import random
import datetime
import time
from CustomExceptions import InDebt

# made global so they can be reused in many methods in the class or outside of the class easily
global twenty_percent_probability
twenty_percent_probability = ["b", "b", "g", "g", "g", "g", "g", "g", "g","g"]  # represents 20% probability of a (b)ad outcome or 80% for a (g)ood one
global thirty_percent_probability
thirty_percent_probability = ["b", "b", "b", "g", "g", "g", "g", "g", "g", "g"]
global fourty_percent_probability
fourty_percent_probability = ["b", "b", "b", "b", "g", "g", "g", "g", "g", "g"]
global sixty_percent_probability
sixty_percent_probability = ["b", "b", "b", "b", "b", "b", "g", "g", "g", "g"]

#class used to set attributes and use methods for pet object
class Animal:

    #constructor/instance variables
    def __init__(self,name, age, species, sex, birthdate, health, happiness = 100, hunger = 100,cash= 50, outcome_message = "outcome message"):
        self.name = name
        self.age = age
        self.species = species
        self.sex = sex
        self.birthdate = birthdate.strftime("%B %d")
        self.health = health
        self.hunger = hunger
        self.happiness = happiness
        self.cash = cash
        self.outcome_message = outcome_message

#_________________________GETTERS____________________________
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_species(self):
        return self.species

    def get_sex(self):
        return self.sex

    def get_birthdate(self):
        return self.birthdate

    def get_health(self):
        return self.health

    def get_hunger(self):
        return self.hunger

    def get_happiness(self):
        return self.happiness

    def get_cash(self):
        return self.cash

    def get_outcome_message(self):
        return self.outcome_message

# _________________________SETTERS____________________________
#these are not exactly (traditional) setters. They basically  adjust the instance variable by adding or subtracting an amount

    def set_age(self,amount):
        self.age = self.age + amount

    def set_health(self,amount):
        self.health = self.health + amount

    def set_hunger(self,amount):
        self.hunger = self.hunger + amount

    def set_happiness(self,amount):
        self.happiness = self.happiness + amount

    def set_cash(self,amount):
        self.cash = self.cash + amount
        if self.cash < 0:
            raise InDebt()  # custom error, but in theory should never be allowed to reach condition for error to be thrown

#_________________________HELPERS_________________________

    # makes pet 1 day older and the other stats will decrease some every day (like in real like)
    def update_age(self):
        self.set_age(1)
        self.set_health(-2)
        self.set_hunger(-2)
        self.set_happiness(-2)

    # in game, key presses will trigger a call to this method. The parameter (action_name)
    # will specify which action to perform(which action method to call).
    # after calling action method, then calls methods to make sure that non of the life stats have gone over 100(check_max_limit),
    # make a call to update age, and set the outcome_message which will be displayed on screen.
    # if the action methods identified that the cash stat was too low to buy some item to perform the action, it will return None.
    # if None is returned, the outcome_message is "You don't have enough money."
    def perform_action(self,action_name):
        if action_name == "feed pet food":
            action = self.feed_pet_food()
        if action_name == "feed discount pet food":
            action = self.feed_discount_food()
        if action_name == "feed food you scavenged for":
            action =self.scavenge()
        if action_name == "give medicine":
            action =self.give_medicine()
        if action_name == "give magic potion":
            action =self.give_magic_potion()
        if action_name == "home remedy":
            action = self.give_home_remedy()
        if action_name == "play":
            action = self.play()
        if action_name == "pet":
            action = self.pet()
        if action_name == "give toy":
            action =self.give_toy()
        if action_name == "perform pet show":
            action = self.perform_pet_show()
        if action != None:
            self.check_max_limit()
            self.update_age()
            self.outcome_message = action
        else:
            self.outcome_message = "You don't have enough money."

# the following 10 methods are called by the perform_action method. They all function very similarly.
# They (for most) first set the price of an item. Then check to see if the cash stat is high enough to
# buy the item required to carry out the action(if it is an action that requires user to spend cash).
# Some of the actions can have a random out come (good or bad). They set a variable called outcome to choose randomly
# from the lists of probabilities at the top of the file. This is how I went about saying there was a 20% chance that the action will have
# a bad outcome. Depending if the outcome was good or bad, the method will then make a call to the setters to update a stat with either an added
# amount or a subtracted amount. For some methods, this is a random number. It then returns a message indicating a good outcome, a bad outcome,
# or None if the cash was to low to perform action
    def feed_pet_food(self):
        price = 10
        if self.cash >= price:
            self.set_cash(-price)
            self.set_hunger(5)
            return "Your pet ate."
        else:
            return None

    def feed_discount_food(self):
        price = 5
        if self.cash >= price:
            self.set_cash(-price)
            outcome = random.choice(twenty_percent_probability)
            if outcome == "b":
                self.set_hunger(-3)
                return "Your pet did not like this food."
            else:
                self.set_hunger(3)
                return "Your pet ate."
        else:
            return None

    def scavenge(self):
        outcome = random.choice(fourty_percent_probability)
        if outcome == "b":
            self.set_hunger(-random.randint(1, 10))
            return "This food made your pet sick."
        else:
            self.set_hunger(random.randint(1, 15))
            return "Your pet ate."

    def give_medicine(self):
        price = 10
        if self.cash >= price:
            self.set_cash(-price)
            outcome = random.choice(thirty_percent_probability)
            if outcome == "b":
                self.set_health(-random.randint(1, 15))
                return "You gave you pet the wrong kind of medicine."
            else:
                self.set_health(random.randint(1, 15))
                return "The medicine worked. Your pet got better."
        else:
            return None

    def give_magic_potion(self):
        price = 5
        if self.cash >= price:
            self.set_cash(-price)
            outcome = random.choice(sixty_percent_probability)
            if outcome == "b":
                self.set_health(- random.randint(1, 10))
                return "You poisoned your pet slightly."
            else:
                self.set_health(100)
                return "You found a magic cure."
        else:
            return None

    def give_home_remedy(self):
        price = 1
        if self.cash >= price:
            self.set_cash(-price)
            outcome = random.choice(thirty_percent_probability)
            if outcome == "b":
                self.set_health(- 2)
                return "This did not help."
            else:
                self.set_health(3)
                return "Your pet is feeling a little better."
        else:
            return None

    def play(self):
        self.set_happiness(5)
        self.set_hunger(- 1)
        return "Your pet had fun."

    def pet(self):
        self.set_happiness(3)
        return "Your pet got happier."

    def give_toy(self):
        price = 2
        if self.cash >= price:
            self.set_cash(-price)
            outcome = random.choice(twenty_percent_probability)
            if outcome == "b":
                self.set_happiness(- 2)
                return "Your pet did not like the new toy."
            else:
                self.set_happiness(7)
                return "Your pet is feeling a little happier."
        else:
            return None

    #This is pretty similar as the rest of the action methods. It is how user makes money
    def perform_pet_show(self):
        income_amount = random.randint(1, 7)
        self.set_hunger(- 1)
        self.set_health(- 1)
        self.set_cash(income_amount)
        return "You earned " + str(income_amount) + " dollars from the pet show."

    #This is called at end of perform_action(). It checks if a stat when over the full limit/ 100%, if so, resets it to 100
    def check_max_limit(self): # keeps the stats values from going over 100
        if self.hunger > 100:
            self.hunger = 100
        if self.health > 100:
            self.health = 100
        if self.happiness > 100:
            self.happiness = 100

    # called from the game main loop every time.
    # checks to see if condition is met for pet to be dead (die of old age or from neglect/abuse)
    def check_for_death(self):
        is_dead = False
        if self.age ==100:
            is_dead = True
        if self.hunger <= 0:
            is_dead = True
        if self.health <= 0:
            is_dead = True
        if self.happiness <= 0:
            is_dead = True
        return is_dead

    def __repr__(self):
        return (repr(self.name) + " " + repr(self.age) + " " + repr(self.species)+ " " + repr(self.sex) + " " + repr(self.birthdate) + " " + repr(self.health) + " " + repr(self.hunger) + " " + repr(self.happiness) + " " + repr(self.cash) )

    def __str__(self):
        return (str(self.name) + " " + str(self.age) + " " + str(self.species)+ " " + str(self.sex) + " " + str(self.birthdate) + " " + str(self.health) + " " + str(self.hunger) + " " + str(self.happiness) + " " + str(self.cash) )
