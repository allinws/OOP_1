my_list = [{'first_name': 'Johan', 'last_name': 'Svensson'}, {'first_name': 'Kalle', 'last_name': 'Johansson'}, {'first_name': 'Johan', 'last_name': 'Lindström'}]

def return_list_last_names(a_list, first_name):
    last_name_list = []
    for item in a_list:
        if item['first_name'] == first_name:
            last_name_list.append(item['last_name'])
    return last_name_list


last_names = return_list_last_names(my_list, 'Johan')

print('Last names for person named Johan', last_names)

