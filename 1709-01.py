Str1 = input("Input First String : ")
Str2 = input("Input Second String : ")
L1 = len(Str1)
L2 = len(Str2)
Ans = -1

for i in range(L2-L1+1):
    Check = 1
    for j in range(L1):
        if Str1[j] != Str2[i+j]:
            Check = 0
    if Check == 1:
        Ans = 1
        break
print(Ans)