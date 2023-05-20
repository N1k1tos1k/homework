import random
my_list=[]
for i in range(10):
    my_list.append(random.randint(1,100))
print(my_list)
print("Четные числа из списка: ")
for i in range(10):
    if (my_list[i]%2==0):
        print(my_list[i])