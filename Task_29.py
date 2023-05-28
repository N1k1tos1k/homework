def reverse_string(string):
    res = ""
    for i in reversed(string):
        res += i
    return res


reverse_string1 = reverse_string("Строка")

print(reverse_string1)

