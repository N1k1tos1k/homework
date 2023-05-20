import random
my_list=[]
for i in range(10):
    my_list.append(random.randint(1,10))
print(my_list)
print('Какое число найти?')
if (my_list.count(int(input()))==0):
    print("Число не найдено в массиве")
else:
    print("Число найдено в массиве")
