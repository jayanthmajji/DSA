x = int(input("enter the number:"))

if x <= 0:
    print("enter a positive number:")
elif x == 1:
    print(0)
elif x == 2:
    print(1)
else:
    print((x-1) + (x-2))
