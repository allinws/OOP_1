""" Övning 2 """

# 1)
a = 10
b = 5

if a > 6:
    print('a is greater than 6')
else:
    print('a is less than 6')


# 2)
for x in range(0,11):
    print(x)

# 3)
counter = 0
while counter < 21:
    print(counter)
    counter = counter +1

# 4)
counter_2 = 0
while counter_2 < 8:
    if counter_2 == 4 or counter_2 == 5:
        counter_2 = counter_2 + 1
        continue
    print(counter_2)
    counter_2 = counter_2 + 1
