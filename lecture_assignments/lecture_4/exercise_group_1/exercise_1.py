my_list = [52, 33, 66, 22, 55, 77, 123, 23, 77, 55, 16, 34, 21]
new_list = []

def add_to_new_list_return_mean_of_new_list(a_list):
    for item in a_list:
        if item > 30:
            new_list.append(item)

    return sum(new_list) / len(new_list)


mean_new_list = add_to_new_list_return_mean_of_new_list(my_list)
print('Mean of new list is', mean_new_list)


# Operators
# Comparison, Arithmetic, Assignmnet

# Flow control statements:
# Iterative, Conditional

# Datastructures:
# Lists

# Datatypes:
# Float, Int, string


