my_list = [52, 33, 66, 22, 55, 77, 123, 23, 77, 55, 16, 34, 21]

my_list = sorted(my_list)

new_list = []

for item in my_list:
    if item > 50 and item < 60:
        continue
    if item > 70:
        break
    new_list.append(item)

print('my_list', my_list)
print('new_list', new_list)




# Operators
# Comparison

# Flow control statements:
# Iterative, Conditional, Transfer

# Datastructures:
# Lists

# Datatypes:
# String, Int

