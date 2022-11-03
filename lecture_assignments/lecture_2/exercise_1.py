""" Övning - funktioner """

# 1

def print_person(first_name, last_name, age, area):
    return f'{first_name} {last_name} is {age} years old and live in {area}'

my_person = print_person(first_name='Alexander', last_name='Lindgren', age=32, area='Stockholm')


# 2
my_list = [1,2,3,4,5,6]

def print_list_items(list):
    for item in list:
        print(item)

print_list_items(list=my_list)


# 3
my_other_list = [5,6,7,8,9,10]

def return_first_three_items(list):
    return list[0:3]

first_three_items = return_first_three_items(my_other_list)
print(first_three_items)