""" Övning - Klasser - Grupper om 3  """

# 1

class MyCar():

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def return_brand_and_model(self):
        return f'Car brand is {self.brand} and model is {self.model}'

    
my_car_instance = MyCar(brand='Toyota', model='Yaris')
my_string = my_car_instance.return_brand_and_model()
print(my_string)


# 2


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def return_year_born(self):
        return 2022-self.age

    def print_year_born(self):
        year_born = self.return_year_born()
        print(year_born)


person_1 = Person(name='johan', age=25)
person_1.print_year_born()
person_2 = Person(name='felix', age=22)
person_2.print_year_born()
person_3 = Person(name='johanna', age=32)
person_3.print_year_born()
