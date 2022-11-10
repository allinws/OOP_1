class Person():

    def __init__(self, name=None, age=None):
        self.name = None
        self.age = None

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError('You need to provide a name in form of a string')

    def set_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError('You need to provide an age in form of an int')



