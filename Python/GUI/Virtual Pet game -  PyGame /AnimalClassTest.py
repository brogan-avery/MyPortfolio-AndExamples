"""
Created on: Apr  20

@author: Brogan Avery

title: Animal Class Test

desc: tests for the animal class
"""

import unittest
from AnimalClass import *
import AnimalClass as ac
from AnimalClass import Animal
import datetime
import random
from unittest.mock import patch
from CustomExceptions import InDebt


#___**___**__TEST WILL FAIL WITHOUT UPDATING THE BIRTHDATE STRING IN THE TEST METHOD TO REFLECT TODAYS DATE!!!!!!!!!!!

class MyTestCase(unittest.TestCase):

    def setUp(self):
        #these objects represent some possible realistic options at different points in the game
        self.testNewPet = Animal("Fido", 0, "dog", "male", datetime.datetime.now().date(),100,100,100,50,"this is the message")
        self.testBrokePet = Animal("Rocky", 0, "dog", "male", datetime.datetime.now().date(),100,100,100,0,"")
        self.testRandomPet = Animal("Marge", 10, "dog", "female", datetime.datetime.now().date(), 50, 50, 50, 40, "")
        self.testDeadPet1 = Animal("Spike", 20, "rodent", "male", datetime.datetime.now().date(), 100, 100, 0, 10, "")
        self.testDeadPet2 = Animal("Fifi", 30, "cat", "female", datetime.datetime.now().date(), 100, 0, 100, 10, "")
        self.testDeadPet3 = Animal("Rover", 40, "dog", "male", datetime.datetime.now().date(), 0, 100, 100, 10, "")

    def tearDown(self):
        del self.testNewPet
        del self.testRandomPet
        del self.testBrokePet
        del self.testDeadPet1
        del self.testDeadPet2
        del self.testDeadPet3

    def test_get_name(self):
        self.assertEqual(self.testNewPet.get_name(),"Fido")

    def test_get_age(self):
        self.assertEqual(self.testNewPet.get_age(), 0)

    def test_get_species(self):
        self.assertEqual(self.testNewPet.get_species(), "dog")

    def test_get_sex(self):
        self.assertEqual(self.testNewPet.get_sex(), "male")

    def test_get_birthdate(self):
        self.assertEqual(self.testNewPet.get_birthdate(), "May 06") #will need to be changed to today to pass

    def test_get_health(self):
        self.assertEqual(self.testNewPet.get_health(), 100)

    def test_get_hunger(self):
        self.assertEqual(self.testNewPet.get_hunger(), 100)

    def test_get_happiness(self):
        self.assertEqual(self.testNewPet.get_happiness(), 100)

    def test_get_cash(self):
        self.assertEqual(self.testNewPet.get_cash(), 50)

    def test_get_outcome_message(self):
        self.assertEqual(self.testNewPet.get_outcome_message(),"this is the message")

    def test_set_age(self):
        self.testRandomPet.set_age(1)
        self.assertEqual(self.testRandomPet.age, 11)

    def test_set_health_add(self):
        self.testRandomPet.set_health(5)
        self.assertEqual(self.testRandomPet.health, 55)

    def test_set_health_subtract(self):
        self.testRandomPet.set_health(-5)
        self.assertEqual(self.testRandomPet.health, 45)

    def test_set_hunger_add(self):
        self.testRandomPet.set_hunger(5)
        self.assertEqual(self.testRandomPet.hunger, 55)

    def test_set_hunger_subtract(self):
        self.testRandomPet.set_hunger(-5)
        self.assertEqual(self.testRandomPet.hunger, 45)

    def test_set_happiness_add(self):
        self.testRandomPet.set_happiness(5)
        self.assertEqual(self.testRandomPet.happiness, 55)

    def test_set_happiness_subtract(self):
        self.testRandomPet.set_happiness(-5)
        self.assertEqual(self.testRandomPet.happiness, 45)

    def test_set_cash_add(self):
        self.testRandomPet.set_cash(5)
        self.assertEqual(self.testRandomPet.cash, 45)

    def test_set_cash_subtract(self):
        self.testRandomPet.set_cash(-5)
        self.assertEqual(self.testRandomPet.cash, 35)

    def test_feed_pet_food(self):
        self.assertEqual(self.testNewPet.feed_pet_food(), "Your pet ate.")
        self.assertEqual(self.testBrokePet.feed_pet_food(), None)

    @patch('random.choice')
    def test_feed_discount_food_good(self,mocked_choice):
        mocked_choice.return_value = 'g'
        self.assertEqual(self.testNewPet.feed_discount_food(), "Your pet ate.")

    @patch('random.choice')
    def test_feed_discount_food_bad(self, mocked_choice):
        mocked_choice.return_value = 'b'
        self.assertEqual(self.testNewPet.feed_discount_food(), "Your pet did not like this food.")

    def test_feed_discount_food_broke(self):
        self.assertIsNone(self.testBrokePet.feed_discount_food())

    @patch('random.choice')
    def test_scavenge_good(self,mocked_choice):
        mocked_choice.return_value = 'g'
        self.assertEqual(self.testNewPet.scavenge(),"Your pet ate.")

    @patch('random.choice')
    def test_scavenge_bad(self,mocked_choice):
        mocked_choice.return_value = 'b'
        self.assertEqual(self.testNewPet.scavenge(),"This food made your pet sick." )

    @patch('random.choice')
    def test_give_medicine_good(self,mocked_choice):
        mocked_choice.return_value = 'g'
        self.assertEqual(self.testNewPet.give_medicine(),"The medicine worked. Your pet got better." )

    @patch('random.choice')
    def test_give_medicine_bad(self,mocked_choice):
        mocked_choice.return_value = 'b'
        self.assertEqual(self.testNewPet.give_medicine(), "You gave you pet the wrong kind of medicine.")

    def test_give_medicine_broke(self):
        self.assertIsNone(self.testBrokePet.give_medicine())

    @patch('random.choice')
    def test_give_magic_potion_good(self,mocked_choice):
        mocked_choice.return_value = 'g'
        self.assertEqual(self.testNewPet.give_magic_potion(),"You found a magic cure." )

    @patch('random.choice')
    def test_give_magic_potion_bad(self,mocked_choice):
        mocked_choice.return_value = 'b'
        self.assertEqual(self.testNewPet.give_magic_potion(),"You poisoned your pet slightly." )

    def test_give_magic_potion_broke(self):
        self.assertIsNone(self.testBrokePet.give_magic_potion())

    @patch('random.choice')
    def test_give_home_remedy_good(self,mocked_choice):
        mocked_choice.return_value = 'g'
        self.assertEqual(self.testNewPet.give_home_remedy(),"Your pet is feeling a little better." )

    @patch('random.choice')
    def test_give_home_remedy_bad(self,mocked_choice):
        mocked_choice.return_value = 'b'
        self.assertEqual(self.testNewPet.give_home_remedy(),"This did not help." )

    def test_give_home_remedy_broke(self):
        self.assertIsNone(self.testBrokePet.give_home_remedy())

    def test_play(self):
        self.assertEqual(self.testNewPet.play(), "Your pet had fun.")
        self.assertEqual(self.testBrokePet.play(), "Your pet had fun.")

    def test_pet(self):
        self.assertEqual(self.testNewPet.pet(), "Your pet got happier.")
        self.assertEqual(self.testBrokePet.pet(), "Your pet got happier.")

    @patch('random.choice')
    def test_give_toy_good(self,mocked_choice):
        mocked_choice.return_value = 'g'
        self.assertEqual(self.testNewPet.give_toy(),"Your pet is feeling a little happier." )

    @patch('random.choice')
    def test_give_toy_bad(self,mocked_choice):
        mocked_choice.return_value = 'b'
        self.assertEqual(self.testNewPet.give_toy(),"Your pet did not like the new toy." )

    def test_give_toy_broke(self):
        self.assertIsNone(self.testBrokePet.give_toy())
        
    def test_update_age(self):
        self.testNewPet.update_age()
        self.assertEqual(self.testNewPet.hunger, 98)
        self.assertEqual(self.testNewPet.health, 98)
        self.assertEqual(self.testNewPet.happiness, 98)
        self.assertEqual(self.testNewPet.age, 1)

    def test_check_for_death(self):
        self.assertFalse(self.testNewPet.check_for_death())
        self.assertFalse(self.testBrokePet.check_for_death())
        self.assertTrue(self.testDeadPet1.check_for_death())
        self.assertTrue(self.testDeadPet2.check_for_death())
        self.assertTrue(self.testDeadPet3.check_for_death())

     #the following tests test the class method that basically controlls all other methods
    #the perform action method will call another method to do an action and then at the end it calls the methods to update age,
    # check the max stat limit of 100, and checks to see if the pet is dead, will also prevent these from happening if there is no money

    def test_perform_action_feed_pet_food(self):
        self.testRandomPet.perform_action("feed pet food")
        self.assertEqual(self.testRandomPet.hunger, 53)
        self.assertEqual(self.testRandomPet.health, 48)
        self.assertEqual(self.testRandomPet.happiness, 48)
        self.assertEqual(self.testRandomPet.cash, 30)
        self.assertEqual(self.testRandomPet.age, 11)

        self.testNewPet.perform_action("feed pet food")     #tests to make sure check_max_limit() is called correctly at the end of the perform action method to show that that method will not let the stats go over 100
        self.assertEqual(self.testNewPet.hunger, 98)
        self.assertEqual(self.testNewPet.health, 98)
        self.assertEqual(self.testNewPet.happiness, 98)
        self.assertEqual(self.testNewPet.cash, 40)
        self.assertEqual(self.testNewPet.age, 1)

        self.testBrokePet.perform_action("feed pet food")  # test shows that nothing will happen if the user does not have enough money for action, instead of getting the outcome message from a return value it uses a default one found in the perform action method
        self.assertEqual(self.testBrokePet.hunger, 100)
        self.assertEqual(self.testBrokePet.health, 100)
        self.assertEqual(self.testBrokePet.happiness, 100)
        self.assertEqual(self.testBrokePet.cash, 0)
        self.assertEqual(self.testBrokePet.age, 0)
        self.assertEqual(self.testBrokePet.outcome_message, "You don't have enough money.") #if user has money, this message will come from the return value of the specific action method that was called

    @patch('random.choice')
    def test_perform_action_feed_discount_pet_food(self,mocked_choice):
        mocked_choice.return_value = 'g'
        self.testRandomPet.perform_action("feed discount pet food")
        self.assertEqual(self.testRandomPet.hunger, 51)
        self.assertEqual(self.testRandomPet.health, 48)
        self.assertEqual(self.testRandomPet.happiness, 48)
        self.assertEqual(self.testRandomPet.cash, 35)
        self.assertEqual(self.testRandomPet.age, 11)

    @patch('random.choice')
    @patch('random.randint')
    def test_perform_action_scavenge(self,mocked_randint,mocked_choice):
        mocked_choice.return_value = 'g'
        mocked_randint.return_value = 2
        self.testRandomPet.perform_action("feed food you scavenged for")
        self.assertEqual(self.testRandomPet.hunger,50)
        self.assertEqual(self.testRandomPet.health, 48)
        self.assertEqual(self.testRandomPet.happiness, 48)
        self.assertEqual(self.testRandomPet.cash, 40)
        self.assertEqual(self.testRandomPet.age, 11)

    @patch('random.choice')
    @patch('random.randint')
    def test_perform_action_give_medicine(self,mocked_randint,mocked_choice):
        mocked_choice.return_value = 'g'
        mocked_randint.return_value = 2
        self.testRandomPet.perform_action("give medicine")
        self.assertEqual(self.testRandomPet.hunger, 48)
        self.assertEqual(self.testRandomPet.health, 50)
        self.assertEqual(self.testRandomPet.happiness, 48)
        self.assertEqual(self.testRandomPet.cash, 30)
        self.assertEqual(self.testRandomPet.age, 11)

    @patch('random.choice')
    @patch('random.randint')
    def test_perform_action_give_magic_potion_bad(self,mocked_randint,mocked_choice):
        mocked_choice.return_value = 'b'
        mocked_randint.return_value = -2
        self.testRandomPet.perform_action("give magic potion")
        self.assertEqual(self.testRandomPet.hunger, 48)
        self.assertEqual(self.testRandomPet.health, 50)
        self.assertEqual(self.testRandomPet.happiness, 48)
        self.assertEqual(self.testRandomPet.cash, 35)
        self.assertEqual(self.testRandomPet.age, 11)

    @patch('random.choice')
    def test_perform_action_give_magic_potion_good(self,mocked_choice):
        mocked_choice.return_value = 'g'
        self.testRandomPet.perform_action("give magic potion")
        self.assertEqual(self.testRandomPet.hunger, 48)
        self.assertEqual(self.testRandomPet.health, 98)
        self.assertEqual(self.testRandomPet.happiness, 48)
        self.assertEqual(self.testRandomPet.cash, 35)
        self.assertEqual(self.testRandomPet.age, 11)

    @patch('random.choice')
    def test_perform_action_give_home_remedy_bad(self,mocked_choice):
        mocked_choice.return_value = 'b'
        self.testRandomPet.perform_action("home remedy")
        self.assertEqual(self.testRandomPet.hunger, 48)
        self.assertEqual(self.testRandomPet.health, 46)
        self.assertEqual(self.testRandomPet.happiness, 48)
        self.assertEqual(self.testRandomPet.cash, 39)
        self.assertEqual(self.testRandomPet.age, 11)

    @patch('random.choice')
    def test_perform_action_give_home_remedy_good(self, mocked_choice):
        mocked_choice.return_value = 'g'
        self.testRandomPet.perform_action("home remedy")
        self.assertEqual(self.testRandomPet.hunger, 48)
        self.assertEqual(self.testRandomPet.health, 51)
        self.assertEqual(self.testRandomPet.happiness, 48)
        self.assertEqual(self.testRandomPet.cash, 39)
        self.assertEqual(self.testRandomPet.age, 11)

    def test_perform_action_play(self):
        self.testRandomPet.perform_action("play")
        self.assertEqual(self.testRandomPet.hunger, 47)
        self.assertEqual(self.testRandomPet.health, 48)
        self.assertEqual(self.testRandomPet.happiness, 53)
        self.assertEqual(self.testRandomPet.cash, 40)
        self.assertEqual(self.testRandomPet.age, 11)

    def test_perform_action_pet(self):
        self.testRandomPet.perform_action("pet")
        self.assertEqual(self.testRandomPet.hunger, 48)
        self.assertEqual(self.testRandomPet.health, 48)
        self.assertEqual(self.testRandomPet.happiness, 51)
        self.assertEqual(self.testRandomPet.cash, 40)
        self.assertEqual(self.testRandomPet.age, 11)

    @patch('random.choice')
    def test_perform_action_give_toy_bad(self, mocked_choice):
        mocked_choice.return_value = 'b'
        self.testRandomPet.perform_action("give toy")
        self.assertEqual(self.testRandomPet.hunger, 48)
        self.assertEqual(self.testRandomPet.health, 48)
        self.assertEqual(self.testRandomPet.happiness,46)
        self.assertEqual(self.testRandomPet.cash, 38)
        self.assertEqual(self.testRandomPet.age, 11)

    @patch('random.choice')
    def test_perform_action_give_toy_good(self, mocked_choice):
        mocked_choice.return_value = 'g'
        self.testRandomPet.perform_action("give toy")
        self.assertEqual(self.testRandomPet.hunger, 48)
        self.assertEqual(self.testRandomPet.health, 48)
        self.assertEqual(self.testRandomPet.happiness,55)
        self.assertEqual(self.testRandomPet.cash, 38)
        self.assertEqual(self.testRandomPet.age, 11)

    @patch('random.randint')
    def test_perform_action_perform_pet_show(self,mocked_randint):
        mocked_randint.return_value = 3
        self.testRandomPet.perform_action("perform pet show")
        self.assertEqual(self.testRandomPet.hunger, 47)
        self.assertEqual(self.testRandomPet.health, 47)
        self.assertEqual(self.testRandomPet.happiness,48)
        self.assertEqual(self.testRandomPet.cash, 43)
        self.assertEqual(self.testRandomPet.age, 11)

    # the above section of tests test for the final expected values for each numeric instance variable at the end of each round
    # (they include the effects of the action, the change in age and the associated effects of age, and also factor in the method that
    # does not allow the life stats to go over 100%). Because all of those tests pass as expected (or fail when expected), it can be assumed that
    # the action methods are functioning correctly. I also chose not to set up tests for the values they change at that level because it is not super helpful
    # in seeing how the game is actually running because these values will never be seen or used by the user at this point since they have to finish running through
    # the perform action method which will change them again. I just included one to show why the information gotten from these tests, while correct, is actually more confusing than it is helpful,
    # especially since if anything was functioning unexpectedly in the action methods, it would be reviled in the above section of tests.
    def test_feed_pet_food_stat_change(self):
        self.testNewPet.feed_pet_food() #these do have an effect on the cash but that is shown with the return value and in the above section of tests
        self.assertEqual(self.testNewPet.hunger,105) #this would be correct but this method is only called from another method which does not let it go over 100, also loses 2 from each stat every day

    def test_InDebt(self):
        with self.assertRaises(InDebt):
            self.testRandomPet.set_cash(-100)

if __name__ == '__main__':
    unittest.main()
