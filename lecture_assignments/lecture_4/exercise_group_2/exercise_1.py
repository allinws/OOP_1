my_list = [52, 33, 66, 22, 55, 77, 123, 23, 77, 55, 16, 34, 21]
my_dict = {'important_numbers': [52, 33]} 

def get_important_numbers(a_dict):
    try:
        return a_dict['important_numbers']
    except KeyError:
        return 0

def check_if_numbers_present(subset_list, full_list):
    for item in subset_list:
        if item not in full_list:
            return False
    return True


important_numbers = get_important_numbers(my_dict)
all_numbers_present = check_if_numbers_present(important_numbers, my_list)
print('Are all important numbers are present in my_list?', all_numbers_present)


# Operators
# Membership

# Flow control statements:
# Iterative, Conditional,

# Datastructures:
# Lists, Dicts

# Datatypes:
# String, Int

