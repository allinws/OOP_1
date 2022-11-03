""" Övning - Exceptions """
print('\n')

# 1

my_dict = {'hej': 1, 'johan': 3}

try:
    print(my_dict['jocke'])
except:
    print('Some exception happened')

print('\n')

# 2

my_list = [1,2,3,4]

try:
    print(my_list[9])
except:
    print('Some exception happened')

print('\n')


# 3 

def create_index_error(value):
    my_list = [1,2,3]
    return my_list[value]

def create_type_error(value):
    x = 'hello'
    return x+value

def create_attribute_error():
    x = 'hi there'
    return x.hello

try:
    create_index_error(2) # Testa här skicka in en siffra som hamnar utanför indexet på listan
    create_type_error('hello') # Testa här skicka in en int istället
    create_attribute_error()
except IndexError:
    print('IndexError happened')
except TypeError:
    print('TypeError happened')
except:
    print('General exception happened')

