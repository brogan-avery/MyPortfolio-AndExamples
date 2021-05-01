import unittest
import LabCode.StackLab.Stack as lc

from LabCode.StackLab.StackEmptyException import StackEmptyException
from LabCode.StackLab.StackFullException import StackFullException


class MyTestCase(unittest.TestCase):
        
    def test_create_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        # ACT
        actual = my_stack.is_empty()
        # ASSERT
        self.assertTrue(actual)

    def test_is_empty_true(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        expected = True
        # ACT
        actual = my_stack.is_empty()
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_is_empty_false(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        item = "Python is Fun!"
        # ACT
        my_stack.push(item)
        actual = my_stack.is_empty()
        expected = False
        # ASSERT
        self.assertEqual(expected, actual)
                
    def test_is_full_True(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        item = "Python is Fun!"
        # ACT
        my_stack.push(item)
        actual = my_stack.is_full()
        expected = True
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_is_full_False(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        expected = False
        # ACT
        actual = my_stack.is_full()
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_push_stack(self):
        # ARRANGE
        my_stack = lc.Stack(2)
        item = "StackItem"
        expected = "StackItem2"
        # ACT
        my_stack.push(item + "1")
        my_stack.push(item + "2")
        actual = my_stack.peek()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_push_full_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        item = "StackItem"
        # ACT
        # ASSERT
        self.assertRaises(StackFullException, my_stack.push(item))
     
    def test_pop_stack(self):
        # ARRANGE
        my_stack = lc.Stack(2)
        item = "StackItem"
        expected1 = "StackItem2"
        expected2 = "StackItem1"
        my_stack.push(item+"1")
        my_stack.push(item+"2")
        # ACT
        actual1 = my_stack.pop()
        actual2 = my_stack.pop()
        # ASSERT
        self.assertEqual(expected1, actual1)
        self.assertEqual(expected2, actual2)

    def test_stack_size_zero(self):
        # ARRANGE
        my_stack = lc.Stack(2)
        expected = 0
        # ACT
        actual = my_stack.size()
        # ASSERT
        self.assertEqual(expected, actual)

    def test_stack_size_non_zero(self):
        # ARRANGE
        my_stack = lc.Stack(2)
        item = "StackItem"
        expected = 2
        # ACT
        my_stack.push(item + "1")
        my_stack.push(item + "2")
        actual = my_stack.size()
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_pop_empty_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        # ACT
        # ASSERT
        with self.assertRaises(StackEmptyException):
            my_stack.pop()
        
    def test_peek_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        item = "StackItem"
        # ACT
        my_stack.push(item)
        expected = item
        actual = my_stack.peek()
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_peek_empty_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        # ACT
        # ASSERT
        with self.assertRaises(StackEmptyException):
            my_stack.peek()

    def test_print_stack_up(self):
        # ARRANGE
        my_stack = lc.Stack(2)
        item = "StackItem"
        expected = "StackItem1\nStackItem2\n"
        # ACT
        my_stack.push(item + "1")
        my_stack.push(item + "2")
        actual = my_stack.print_stack_up()
        # ASSERT
        self.assertEqual(expected, actual)
        
    def test_print_stack_up_empty_stack(self):
        # ARRANGE
        my_stack = lc.Stack(1)
        # ACT
        # ASSERT
        with self.assertRaises(StackEmptyException):
            my_stack.print_stack_up()


if __name__ == '__main__':
    unittest.main()
