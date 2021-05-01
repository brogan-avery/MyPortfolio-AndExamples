"""
Created on: May 3

@author: Brogan Avery

title: Sub Classes Test

desc: tests for the animal sub classes
"""

import unittest
from SubClasses import Dog
from SubClasses import Cat
from SubClasses import Rodent
from SubClasses import *
import SubClasses as sc
import AnimalClass
from AnimalClass import Animal
import datetime

class MyTestCase(unittest.TestCase):

#___**___**__TEST WILL FAIL WITHOUT UPDATING THE BIRTHDATE STRING IN THE TEST METHOD TO REFLECT TODAYS DATE!!!!!!!!!!!

# ideally I probably would have put these all in there own test file, but since they aren't doing a whole lot, I just did it as one.

    def setUp(self):
        self.testNewDog = Dog("Fido", 0, "dog", "male", datetime.datetime.now().date(), 100, 100, 100, 50,"outcome message","Bark")
        self.testNewCat = Cat("Rex", 0, "cat", "male", datetime.datetime.now().date(), 100, 100, 100, 50,"outcome message","Meow")
        self.testNewRodent = Rodent("Mini", 0, "rodent", "female", datetime.datetime.now().date(), 100, 100, 100, 50,"outcome message","Squeak")

    def tearDown(self):
        del self.testNewDog
        del self.testNewCat
        del self.testNewRodent


    def test_inital_attributes(self):
        self.assertEqual(self.testNewDog.name, "Fido")
        self.assertEqual(self.testNewDog.age, 0)
        self.assertEqual(self.testNewDog.species, "dog")
        self.assertEqual(self.testNewDog.sex, "male")
        self.assertEqual(self.testNewDog.birthdate, "May 06") #CHANGE DATE TO PASS
        self.assertEqual(self.testNewDog.health, 100)
        self.assertEqual(self.testNewDog.hunger, 100)
        self.assertEqual(self.testNewDog.happiness, 100)
        self.assertEqual(self.testNewDog.cash, 50)
        self.assertEqual(self.testNewDog.outcome_message,"outcome message")
        self.assertEqual(self.testNewDog.sound, "Bark")

        self.assertEqual(self.testNewCat.name, "Rex")
        self.assertEqual(self.testNewCat.age, 0)
        self.assertEqual(self.testNewCat.species, "cat")
        self.assertEqual(self.testNewCat.sex, "male")
        self.assertEqual(self.testNewCat.birthdate, "May 06")  # CHANGE DATE TO PASS
        self.assertEqual(self.testNewCat.health, 100)
        self.assertEqual(self.testNewCat.hunger, 100)
        self.assertEqual(self.testNewCat.happiness, 100)
        self.assertEqual(self.testNewCat.cash, 50)
        self.assertEqual(self.testNewCat.outcome_message, "outcome message")
        self.assertEqual(self.testNewCat.sound, "Meow")

        self.assertEqual(self.testNewRodent.name, "Mini")
        self.assertEqual(self.testNewRodent.age, 0)
        self.assertEqual(self.testNewRodent.species, "rodent")
        self.assertEqual(self.testNewRodent.sex, "female")
        self.assertEqual(self.testNewRodent.birthdate, "May 06")  # CHANGE DATE TO PASS
        self.assertEqual(self.testNewRodent.health, 100)
        self.assertEqual(self.testNewRodent.hunger, 100)
        self.assertEqual(self.testNewRodent.happiness, 100)
        self.assertEqual(self.testNewRodent.cash, 50)
        self.assertEqual(self.testNewRodent.outcome_message, "outcome message")
        self.assertEqual(self.testNewRodent.sound, "Squeak")

# this is not inside of a class
    def test_make_pet_into_object(self):
        make_pet_into_object("Roger", 0, "cat", "male",datetime.datetime.now().date())
        self.assertEqual(sc.pet.name, "Roger")
        self.assertEqual(sc.pet.age, 0)
        self.assertEqual(sc.pet.species, "cat")
        self.assertEqual(sc.pet.sex, "male")
        self.assertEqual(sc.pet.birthdate, "May 06")  # CHANGE DATE TO PASS
        self.assertEqual(sc.pet.health, 100)
        self.assertEqual(sc.pet.hunger, 100)
        self.assertEqual(sc.pet.happiness, 100)
        self.assertEqual(sc.pet.cash, 50)
        self.assertEqual(sc.pet.outcome_message, "outcome message")
        self.assertEqual(sc.pet.sound, "Meow")

if __name__ == '__main__':
    unittest.main()
