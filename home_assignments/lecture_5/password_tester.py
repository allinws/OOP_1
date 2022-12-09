from my_program import weak_passwords, PasswordChecker
import unittest



class TestPasswordChecker(unittest.TestCase):

    def setUp(self):
        self.checker = PasswordChecker(weak_passwords)

    def test_password_length_fails_if_to_short(self):
        self.checker.password = 'asd'
        ok = self.checker.is_password_length_ok()
        self.assertFalse(ok)

    def test_password_length_passes_if_8_chars(self):
        self.checker.password = 'aaaaaaaa'
        ok = self.checker.is_password_length_ok()
        self.assertTrue(ok)

    def test_password_weak(self):
        self.checker.password = '654321'
        ok = self.checker.is_password_weak()
        self.assertTrue(ok)
    
    def test_password_not_weak(self):
        self.checker.password = 'lamwlksngkjnawda'
        ok = self.checker.is_password_weak()
        self.assertFalse(ok)

    def test_password_not_having_two_numbers(self):
        self.checker.password = 'aaaaaaaa'
        ok = self.checker.has_password_at_least_two_numbers()
        self.assertFalse(ok)

    def test_password_having_two_numbers(self):
        self.checker.password = 'aaaa23aaaa'
        ok = self.checker.has_password_at_least_two_numbers()
        self.assertTrue(ok)

    def test_password_not_having_two_capital_letter(self):
        self.checker.password = 'aaaa23aaaa'
        ok = self.checker.has_password_at_least_two_capital_letters()
        self.assertFalse(ok)

    def test_password_having_two_capital_letter(self):
        self.checker.password = 'aaAA23aaaa'
        ok = self.checker.has_password_at_least_two_capital_letters()
        self.assertTrue(ok)

    def test_password_is__valid(self):
        self.checker.password = '72C4U0v5efcAm49LAAg2'
        errors = self.checker.do_password_validation()
        self.assertEqual(errors, 0)


if __name__ == '__main__':
    unittest.main()
