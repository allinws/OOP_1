import unittest
from my_program_2 import MyClass

class TestMyClass(unittest.TestCase):

    def test_my_class(self):
        instance = MyClass()
        return_value = instance.return_ten()
        self.assertEqual(return_value, 10)

if __name__ == '__main__':
    unittest.main()