ans=input()
k=0
for i in range(2,int(ans)):
    if (int(ans)%i==0):
        k+=1
if (k<=0):
    print("Число простое")
else:
    print("Число не простое")