print("Введите первое число")
a=input()
print("Введите второе число")
b=input()
print("Введите операцию(+/-/%/*)")
c=input()

if (c=='+'):
    print(int(a)+int(b))
elif (c=='-'):
    print(int(a)-int(b))
elif (c=='%'):
    print(int(a)/int(b), ", остаток - ",int(a)%int(b))
elif (c=='*'):
    print(int(a)*int(b))
else: print("Ошибка")