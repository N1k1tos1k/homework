print("Введите первое число")
ans=input()
print("Введите второе число")
ans2=input()
for i in range(2,int(min(ans,ans2))):
    if (int(ans)%i==0) and (int(ans2)%i==0):
        print("Наименьший общий множитель ", i)
        exit()
print("Наименьший общий множитель 1")