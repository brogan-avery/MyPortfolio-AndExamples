import unittest
from Game import make_death_cert

class MyTestCase(unittest.TestCase):

    def test_make_death_cert(self):
        self.assertEqual(make_death_cert(), "A death certificate has been made for your pet.")


if __name__ == '__main__':
    unittest.main()
