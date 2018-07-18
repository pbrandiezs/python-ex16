import string
import random

def gen_password():
    password = []
    for i in range(10):
        a = random.randint(1,3)
        if a == 1:
            password += random.choice(string.ascii_letters)
        if a == 2:
            password += random.choice(string.digits)
        if a == 3:
            password += random.choice(string.punctuation)
    return ("".join(password))

def main():
    print("password is " + str(gen_password()))

main()
