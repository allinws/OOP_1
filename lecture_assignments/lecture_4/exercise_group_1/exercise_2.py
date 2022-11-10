my_dict = {'first_name': 'Johan', 'last_name': 'Henriksson'}

def get_birth_date(a_dict):
    try:
        key = a_dict['birth-date']
        return key
    except KeyError:
        return 0


key = get_birth_date(my_dict)

if key != 0:
    print('Birth date is', key)
else:
    print('Key couldnt be found')


# Operators
# Comparison, Assignment

# Flow control statements:
# Conditional

# Datastructures:
# Dictionary

# Datatypes:
# String, ints

# Errors
# KeyError