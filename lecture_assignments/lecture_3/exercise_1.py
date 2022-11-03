""" ÖVNING - Dict and list comprehension """

# 1
a = 5
print('\n')
print('If example: ')
if a > 3:
    print('a larger than 3')
    a = a + 2
if a > 5:
    print('a larger than 6')

print('\n')

print('Elif example: ')
b = 5
if b > 3:
    print('b larger than 3')
    a = a + 2
elif b > 5:
    print('b larger than 6')


# 2
my_list = [1964, 1935, 1967, 1972, 1905, 1996, 1924, 1937, 1922, 1925, 1924, 1962, 1980, 1922, 1964, 1916, 1941, 1941, 1922, 1937]
new_list = [x for x in my_list if x > 1955]
print(new_list)
print('\n')

# 3

x_list = [1,2,3]
y_list = x_list

print(x_list is y_list)
print('A list saved in a variable is saving the reference to the list in memory, not the actual content of the list')
print('\n')

# 4 

z_list = [1,2,3]
m_list = z_list.copy()

print(z_list is m_list)
print('Copying the list creates a new list, and "is" is checking if they have the same reference, which they dont.')
print('\n')


