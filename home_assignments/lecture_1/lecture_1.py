""" Övning 3 """

# 1)
my_person = {'first_name': 'Alexander', 'last_name': 'Lindgren'}
my_person['birth_date'] = '1990-08-06'

# 2)
my_person_2 = {'first_name': 'Alexander', 'last_name': 'Lindgren'}

if isinstance(my_person_2, dict):
    print('is a dict')
else:
    print('is not a dict')


for key, value in my_person_2.items():
    print(key)
    print(value)


# 3)
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = my_list.copy()
new_list.append(11)
new_list.remove(4)
sliced_list = new_list[0:4]

for item in sliced_list:
    print(item)

print(my_list)
print(len(my_list))


# 4)
my_set_1 = set(new_list)
my_set_2 = set(my_list)
final_set = my_set_1.union(my_set_2)
print(final_set)