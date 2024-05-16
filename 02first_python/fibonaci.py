n = int(input("enter the number:"))

if n <= 0:
    print("Enter a positive  number:")
elif n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    print((n-1) + (n-2))
