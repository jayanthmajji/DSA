n = int(input("enter the year:"))

if n % 400 == 0 and n % 100 == 0:
    print("it is a leap year")
elif n % 4 == 0 and n % 100 != 0:
    print("it is a leap year")
else:
    print("it is not a leap year!")
