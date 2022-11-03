""" Övning - Raise errors """

# 1

def raise_value_error():
    raise ValueError

def raise_index_error():
    raise IndexError

def raise_key_error():
    raise KeyError

try:
    raise_value_error()
except ValueError:
    print('ValueError happened')

try:
    raise_index_error()
except IndexError:
    print('IndexError happened')

try:
    raise_key_error()
except KeyError:
    print('KeyError happened')