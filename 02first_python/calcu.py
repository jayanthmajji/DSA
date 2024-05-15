x = int(input("enter the first number:"))
y = int(input("enter the second number:"))
op = (input("enter the operator:"))

if op == '+':
    print("The sum of two numbers is:", x+y)
elif op == '-':
    print("The difference of two numbers is: ", x-y)
elif op == '*':
    print("The product of two numbers is:", x*y)
elif op == '/':
    print("The division of two numbers is:", x/y)
else:
    print("Invalid operator!!")
