"""
Created on May  1

@author: Brogan Avery

title: sub classes

desc: contains the sub classes of the animal class
"""

# these classes honestly don't really add much value to the game, unless the user forgets their animal sounds...
from AnimalClass import Animal


#DOG
class Dog(Animal):
    def __init__(self,name, age, species, sex, birthdate, health = 100, happiness = 100, hunger = 100,cash= 50, outcome_message = "outcome message", sound = "Bark"):
        super().__init__(name, age, species, sex, birthdate, health = 100, happiness = 100, hunger = 100,cash= 50, outcome_message = "outcome message")

        self.sound = sound

    def __repr__(self):
        return (repr(self.name) + " " + repr(self.age) + " " + repr(self.species) + " " + repr(self.sex) + " " + repr(self.birthdate) + " " + repr(self.health) + " " + repr(self.hunger) + " " + repr(self.happiness) + " " + repr(self.cash)+ " " + repr(self.sound))
    def __str__(self):
        return "Name: " + (str(self.name) + " Age: " + str(self.age) + " Species: " + str(self.species) + " Sex: " + str(self.sex) + " BirthDate: " + str(self.birthdate) + " Health: " + str(self.health) + " Hunger: " + str(self.hunger) + " Happiness: " + str(self.happiness) + " Cash: " + str(self.cash)+ " Sound: " + str(self.sound))

#CAT
class Cat(Animal):
    def __init__(self, name, age, species, sex, birthdate, health=100, happiness=100, hunger=100, cash=50,outcome_message="outcome message", sound = "Meow"):
        super().__init__(name, age, species, sex, birthdate, health=100, happiness=100, hunger=100, cash=50,outcome_message="outcome message")

        self.sound = sound

    def __repr__(self):
        return (repr(self.name) + " " + repr(self.age) + " " + repr(self.species) + " " + repr(self.sex) + " " + repr(self.birthdate) + " " + repr(self.health) + " " + repr(self.hunger) + " " + repr(self.happiness) + " " + repr(self.cash) + " " + repr(self.sound))

    def __str__(self):
        return "Name: " + (str(self.name) + " Age: " + str(self.age) + " Species: " + str(self.species) + " Sex: " + str(self.sex) + " BirthDate: " + str(self.birthdate) + " Health: " + str(self.health) + " Hunger: " + str(self.hunger) + " Happiness: " + str(self.happiness) + " Cash: " + str(self.cash) + " Sound: " + str(self.sound))

#RODENT
class Rodent(Animal):
    def __init__(self, name, age, species, sex, birthdate, health=100, happiness=100, hunger=100, cash=50,outcome_message="outcome message", sound = "Squeak"):
        super().__init__(name, age, species, sex, birthdate, health=100, happiness=100, hunger=100, cash=50,outcome_message="outcome message")

        self.sound = sound

    def __repr__(self):
        return (repr(self.name) + " " + repr(self.age) + " " + repr(self.species) + " " + repr(self.sex) + " " + repr(self.birthdate) + " " + repr(self.health) + " " + repr(self.hunger) + " " + repr(self.happiness) + " " + repr(self.cash) + " " + repr(self.sound))

    def __str__(self):
        return "Name: " + (str(self.name) + " Age: " + str(self.age) + " Species: " + str(self.species) + " Sex: " + str(self.sex) + " BirthDate: " + str(self.birthdate) + " Health: " + str(self.health) + " Hunger: " + str(self.hunger) + " Happiness: " + str(self.happiness) + " Cash: " + str(self.cash) + " Sound: " + str(self.sound))

# used to make new objects by calling the nested methods to make object from the sub class of animal
def make_pet_into_object(name, age, species, sex, birthdate):
    def pet_is_dog():
        dog = Dog(name, age, species, sex, birthdate)
        return dog
    def pet_is_cat():
        cat = Cat(name, age, species, sex, birthdate)
        return cat
    def pet_is_rodent():
        rodent = Rodent(name, age, species, sex, birthdate)
        return rodent

    global pet  # made global to use outside this method throughout the game/program

    if species == "dog":
        pet = pet_is_dog()

    if species == "cat":
        pet = pet_is_cat()

    if species == "rodent":
        pet = pet_is_rodent()

    return pet