

class DogClass():

    def bark(self):
        print('Woff')


class ChihuahuaClass():

    def __init__(self):
        self.dog = DogClass()

    def make_sound(self):
        self.dog.bark()



chiuaua = ChihuahuaClass()
chiuaua.make_sound()
