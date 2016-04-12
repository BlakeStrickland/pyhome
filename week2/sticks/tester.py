#test file
import unittest
from pick_up import TwoPlayer


class GameTester(unittest.TestCase):
    ''' In class examples
    def test_assert_true(self):
        self.assertTrue(my_module.is_true())

    def test_assert_false(self):
        self.assertFalse(my_module.is_false())

    def test_assert_equal(self):
        self.assertEqual(my_module.get_one(), 1)

    def test_assert_not_equal(self):
        self.assertNotEqual(my_module.get_one(), 0)
        '''

    def test_assert_true(self):
        self.assertTrue(True)

    def test_greeting(self):
        self.assertEqual(TwoPlayer.greeting(),"Welcome to the Game of Sticks!")

if __name__ == '__main__':
    unittest.main()
