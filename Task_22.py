import random

my_list=[]
summ=0
for i in range(5):
    my_list.append(random.randint(1,10))
    summ+=my_list[i]
print(my_list)
print(summ)