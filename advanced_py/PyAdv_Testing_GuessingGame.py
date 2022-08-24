import unittest
import PyModules_GuessingGame


class TestMaxNumber(unittest.TestCase):
    def setUp(self):
        print('about to start a function')

    def get_number(self):
        test_param = 50
        max_num = PyModules_GuessingGame.getGuess(test_param)
        self.assertEqual(max_num, 50)

    def get_str(self):
        test_param = 'number'
        max_num = PyModules_GuessingGame.getGuess(test_param)
        self.assertEqual(max_num, 'Please enter a number!')

    def get_empty(self):
        test_param = ''
        max_num = PyModules_GuessingGame.getGuess(test_param)
        self.assertEqual(max_num, 'Please enter a number!')

    def get_empty(self):
        test_param = None
        max_num = PyModules_GuessingGame.getGuess(test_param)
        self.assertEqual(max_num, 'Please enter a number!')

    def tearDown(self):
        print('cleaning up')


class TestGetGuess(unittest.TestCase):
    pass


class TestGuessGame(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
