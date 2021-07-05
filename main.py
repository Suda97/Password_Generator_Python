import random


def passGen(leng):
    signs = "1234567890abcdefghijklmnoprstuwxyzvABCDEFGHIJKLMNOPRSTUWXYZV!@#$%^&*()_+-={}[]:;|.<>/?"
    x = []
    while leng > 0:
        x.append(random.choice(signs))
        leng -= 1
    return x


num = int(input("Number of characters in password: "))
print("".join(passGen(num)))
