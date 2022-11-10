
# 1 

class MyMathClass():

    def return_list_mean(self, input_list):
        if not isinstance(input_list, list):
            raise ValueError
        sum = 0
        for item in input_list:
            sum += item
        return sum/len(input_list)



my_list = [1,2,3,4]
my_set = {1,2,3,4}

instance = MyMathClass()

mean = instance.return_list_mean(my_list)
print(f'The mean of {my_list} is {mean}')

try:
    mean = instance.return_list_mean(my_set)
except ValueError:
    print('Error: You provided something other than a list')

