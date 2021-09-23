print("Monday counter")
x = float(input("What day is the first day of this year?(monday = 1)(tuesday = 2(sunday = 7))"))
y = 0
while x <= 365:
    x = x+7
    y = y+1
print (y)

