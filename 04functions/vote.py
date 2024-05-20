def vote(a):
    if a >= 18:
        return ("Person is able to vote!")
    else:
        return ("Person is not able to vote!")


print(vote(int(input("enter the age:"))))
