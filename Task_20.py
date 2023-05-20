import random

my_list=[]
my_sort=[]
for i in range(10):
    my_list.append(random.randint(1,100))
print(my_list)
my_sort=my_list
my_sort.sort()
print('Наименьшее - ', my_sort[0], ", наибольшее - ", my_sort[9])