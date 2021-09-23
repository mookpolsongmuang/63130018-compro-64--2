print("Calculator program")
x = float(input("please type your first input number"))
y = float(input("please type your second input number"))
z = input("please type your operator + - * / %")
if z == "+":
    a = x+y
elif z == "-":
    a = x-y
elif z == "*":
    a = x*y
elif z == "/":
    a = x/y
elif z == "%":
    a = x%y
print(round(a, 2))
