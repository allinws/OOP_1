
weak_passwords = [
    '123456',
    '123456789',
    'Qwerty',
    'Password',
    '12345',
    '12345678',
    '111111',
    '1234567',
    '123123',
    'Qwerty123',
    '1q2w3e',
    '1234567890',
    'DEFAULT',
    '0',
    'Abc123',
    '654321',
    '123321',
    'Qwertyuiop',
    'Iloveyou',
    '666666',
]


class PasswordChecker():

    def __init__(self, weak_passwords, password=None):
        self.password = password
        self.weak_passwords = weak_passwords

    def is_password_length_ok(self):
        if len(self.password) < 7:
           return False
        return True

    def is_password_weak(self):
        if self.password in self.weak_passwords:
            return True
        return False
    
    def has_password_at_least_two_numbers(self):
        num_counter = 0
        for char in self.password:
            if char.isnumeric():
                num_counter += 1
        if num_counter > 1:
            return True
        return False

    def has_password_at_least_two_capital_letters(self):
        num_capital = 0
        for char in self.password:
            if char.isupper():
                num_capital += 1
        if num_capital > 1:
            return True
        return False

    def do_password_validation(self):
        errors = 0
        if not self.is_password_length_ok():
            errors += 1
            print('Password need to be at least 8 characters')
        if self.is_password_weak():
            errors += 1
            print('Password cannot contain to simple combinations, try another more complex password')
        if not self.has_password_at_least_two_numbers():
            errors += 1
            print('Password need to contain at least two digits')
        if not self.has_password_at_least_two_capital_letters():
            errors += 1
            print('Password need to have at least two capital letters')
        if errors == 0:
            print('Password OK!')
        return errors

