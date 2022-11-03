""" Övning Ärva Klasser - Grupper om 3 """

class Vehicle():

    def __init__(self, color, weight, num_wheels):
        self.color = color
        self.weight = weight
        self.num_wheels = num_wheels

    def return_color(self):
        return self.color

    def return_weight(self):
        return self.weight
    
    def return_num_wheels(self):
        return self.num_wheels()


class Car(Vehicle):

    def __init__(self, color, weight, num_wheels, brand):
        Vehicle.__init__(self, color=color, weight=weight, num_wheels=num_wheels)
        self.brand = brand

    def return_brand(self):
        return self.brand


my_car_instance = Car(color='green', weight=1600, num_wheels=4, brand='Toyota')
color = my_car_instance.return_color()
brand = my_car_instance.return_brand()

print(color)
print(brand)
