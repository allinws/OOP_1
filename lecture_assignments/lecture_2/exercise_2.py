""" Classes enskild """

class Bus():

    def __init__(self, seats):
        self.seats = seats

    def print_seats(self):
        print(self.seats)


my_bus = Bus(seats=25)
my_bus.print_seats()

my_other_bus = Bus(seats=35)
my_other_bus.print_seats()