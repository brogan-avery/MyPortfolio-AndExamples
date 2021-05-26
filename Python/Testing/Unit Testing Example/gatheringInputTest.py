import unittest
import mock
from gatheringInput import *


class MyTestCase(unittest.TestCase):

    def test_get_num_of_scores_valid_int(self):
        with mock.patch('builtins.input', return_value= 5):
            assert get_num_of_scores() == 5

    def test_get_num_of_scores_invalid_int(self):
        with mock.patch('builtins.input', return_value= -5):
            self.assertRaises(TypeError)
            assert get_num_of_scores() == 'You may only enter in the keys 1-9. You must enter in a valid digit above 0.'

    def test_get_num_of_scores_invalid_str(self):
        with mock.patch('builtins.input', return_value= "five"):
            self.assertRaises(TypeError)
            assert get_num_of_scores() == 'You may only enter in the keys 1-9. You must enter in a valid digit above 0.'

    def test_get_num_of_scores_invalid_float(self):
        with mock.patch('builtins.input', return_value= 5.5):
            self.assertRaises(TypeError)


    def test_get_next_score_valid_int(self):
        with mock.patch('builtins.input', return_value= 5):
            assert get_next_score() == 5

    def test_get_next_score_invalid_int(self):
        with mock.patch('builtins.input', return_value= -5):
            self.assertRaises(TypeError)
            assert get_next_score() == 'You may only enter in the keys 0-9. You must enter in a valid digit 0 or above.'

    def test_get_next_score_invalid_str(self):
        with mock.patch('builtins.input', return_value= "five"):
            self.assertRaises(TypeError)
            assert get_next_score() == 'You may only enter in the keys 0-9. You must enter in a valid digit 0 or above.'

    def test_get_next_score_invalid_float(self):
        with mock.patch('builtins.input', return_value= 5.5):
            self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()

