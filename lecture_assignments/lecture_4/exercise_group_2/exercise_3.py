import collections

my_list = [52, 33, 66, 22, 55, 77, 123, 23, 77, 55, 16, 34, 21, 16]
other_list = [5, 2, 1, 2]


def return_count_duplicates(a_list):
    len_list = len(a_list)
    len_set = len(set(a_list))
    return len_list - len_set

def return_duplicates(a_list):
    counts = collections.Counter(a_list)
    duplicates = []
    for number, count in counts.items():
        if count != 1:
            duplicates.append(number)
    return duplicates


def combine_two_lists_into_set(a_list, another_list):
    return set(a_list + another_list)


count_duplicates = return_count_duplicates(my_list)
print('Number of duplicates in list', count_duplicates)

duplicates = return_duplicates(my_list)
print('Duplicate numbers in list', duplicates)

new_set = combine_two_lists_into_set(my_list, other_list)
print('Combined set', new_set)

