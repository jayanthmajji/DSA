a = int(input("enter the first number:"))
b = int(input("enter the  second number:"))

hcf = 1

for i in range(1, a+1):
    if a % i == 0 and b % i == 0:
        hcf = i
print("HCF OF THE TWO NUMBERS IS :", hcf)

lcm = a * b / hcf
print("LCM OF THE TWO NUMERS IS :", lcm)
