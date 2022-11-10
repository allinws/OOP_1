import unittest
from unittest import TestCase

from program import Person


class TestPerson(TestCase):

    def setUp(self):
        self.person = Person()

    def test_setting_name_correctly(self):
        name = 'Johan'
        self.person.set_name(name)
        self.assertEqual(self.person.name, name)
    
    def test_setting_age_correctly(self):
        age = 5
        self.person.set_age(age)
        self.assertEqual(self.person.age, age)

    def test_setting_name_incorrectly(self):
        name = 123
        with self.assertRaises(ValueError):
            self.person.set_name(name)

    def test_setting_age_incorrectly(self):
        age = '15'
        with self.assertRaises(ValueError):
            self.person.set_age(age)



if __name__ == '__main__':
    unittest.main()