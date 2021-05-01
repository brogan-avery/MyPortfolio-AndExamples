
"""
Created on: Apr  1 2020

@author: Brogan Avery 

title: Pick Your Pet

desc: where the user picks/creates a pet
"""

import datetime
import time
import os
from AnimalClass import *
from SubClasses import *
import SubClasses as sc

#this is only for testing the program quickly and making unit tests easier
def quick_play():
    make_pet_into_object("Ginger",0,"dog","female", datetime.datetime.now().date())
test = input("quick play?")
if test == "y":
    quick_play()
else:

# The program tries to read in lines from a file which contain the rules for the game.
#  ***__**_I suggest opening up the actual file to reference when playing the game so you do not have to memorize the key commands_**__***
    file_lines = []
    try:
        with open('GameRules.txt', 'r') as file:  # reads from a file to get game instructions
            for line in file:
                file_lines.append(line)
        for line in file_lines:
            print(line, "\n")
    except IOError:
        print("The file does not exist or could not be accessed")


    species_options ={ 'cat' : 'ฅ(=^ェ^=)ฅ', 'dog' : '▼•ᴥ•▼', 'rodent' : '<:3)~'}      # dictionary of pets and there "icon" for pre game set up

# declares empty/starting variables that will be set by user in this file
    name=''
    species = ''
    sex=''
    age = 0
    icon = species_options.get(species)         # uses the user input for species(key) in species_options dictionary to look up the associated icon(value)
    birthdate = datetime.datetime.now().date()  # datetime.now function of datetime module: sets 'pet birth' to now a.k.a, the day the user created the pet

    print("* * *  * * *  * * *")
    print("Hello and welcome to the pet shelter.")
    print("What kind of animal would you like your pet to be?")
    print("___Pets for Adoption___")
    for key in species_options:  # for loop: prints dictionary key values to show what types of animals the user can choose from
        print("       ", key)
    print("_______________________")

# while loop: Prompts user to enter values until entry matches an option in species_option dictionary
    while (species not in species_options):
        species = input("I want to adopt a: ")
        if (species not in species_options):
            print("You must chose a pet from the list of available pets")
    print(f"Great, a {species} will make a good pet!")

    time.sleep(1)

# while loop: Prompts user to enter values until entry matches an option in list
    sex_options= ["male", "female"]
    while (sex not in sex_options):
        sex = input("Is your pet male or female?")
        if (sex not in sex_options):
            print("You must chose male or female")
    print(f"Congratulations! you are now the parent of a new {sex} {species}")

# if/else: creates the appropriate pronouns for pet
    if (sex == "male"):
        pronoun1 = "he"
    else:
        pronoun1 = "she"

    if (sex == "male"):
        pronoun2 = "him"
    else:
        pronoun2 = "her"

    print("*   *   *  *")

    time.sleep(1)

# Prompts user to create pet name from only alpha key characters, then capitalizes it
    while (name.isalpha() == False):
        name = input("Now its time to name your pet. \nMy pet's name is:")
    name = name.capitalize()

# prints out all the information the user has entered to create pet in a 'pet stats'-like format
    print ( f"Here is your pet's information :\n    {species_options[species]}\n    name: {name}\n    sex: {sex}\n    species: {species}\n    born on: {birthdate}\n    age: {age} days old\n")
    time.sleep(3)
    print (f"Make sure to care for your pet or {pronoun1} could get sick, sad, hungry, and even die if you neglect {pronoun2}.")
    print("*   *   *  *")
    time.sleep(2)

    print("Lets start the game.......")
    time.sleep(2)

# makes call to method in the SubClasses file to create new pet object of Animal super class
# prints just to show that the pet object was correctly created with the animal class and sub class object variables.
    print(make_pet_into_object(name, age, species, sex, birthdate))
