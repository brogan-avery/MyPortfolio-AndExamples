from django.test import TestCase
from django.test import Client
import unittest
from nose.tools import assert_true
from exercise import views
from .views import *

class MyTestCase(TestCase):
    # setting up a test object for the classes in the .models file
    def setUp(self):
        self.actionEntry = Actions.objects.create(action='push-up', cat='strength' , targetArea='arms')
        self.planEntry = Plan.objects.create(name='plan1',action='push-up', reps=5, time=0, order=0)

    def tearDown(self):
        del self.actionEntry
        del self.planEntry

    def test_action_entry_creation(self):
        self.assertEqual(self.actionEntry.action, 'push-up')
        self.assertEqual(self.actionEntry.cat, 'strength')
        self.assertEqual(self.actionEntry.targetArea, 'arms')

    def test_plan_entry_creation(self):
        self.assertEqual(self.planEntry.action, 'push-up')
        self.assertEqual(self.planEntry.reps, 5)
        self.assertEqual(self.planEntry.time, 0)
        self.assertEqual(self.planEntry.order, 0)
        self.assertEqual(self.planEntry.name, 'plan1')

if __name__ == '__main__':
    unittest.main()