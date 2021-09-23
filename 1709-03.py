x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a=0
b=0
for i in range (12):
    for j in range (x[i]):
        if  (j+1)%2==1:
            a = a+1
        else :
            b = b+1
print("Travel by nokair = ",a,"days")
print("Travel by air asea = ",b,"days")