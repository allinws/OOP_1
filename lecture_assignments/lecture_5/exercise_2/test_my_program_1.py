import unittest
from my_program import return_a_string


class TestString(unittest.TestCase):
    
    def test_func_returns_string(self):
        is_this_a_string = return_a_string()
        self.assertIsInstance(is_this_a_string, str)

if __name__ == '__main__':
    unittest.main()
