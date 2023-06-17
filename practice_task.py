# Написать программу, которая принимает на вход строку и выводит на экран количество различных
# подстрок строки, начинающихся и заканчивающихся одним и тем же символом.

import string

user_string = str(input("Напишите строку: "))
result_list = []

# Работа с пунктуацией
clear_string = user_string.translate(str.maketrans('', '', string.punctuation))

# список подстрок
substrings = clear_string.split()

# сверяем подстроки
for str in substrings:
    if str[0] == str[-1]:
        result_list.append(str)

# вывод
if len(result_list):
    print(f"Подстроки, начинающиеся и заканчивающиеся одинаковыми символами:")
    print(*result_list, sep='\n')
else:
    print("В строке нет подстрок")