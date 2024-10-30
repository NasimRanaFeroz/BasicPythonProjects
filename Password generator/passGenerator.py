import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_pass():
    pass_lenth = int(input("How long would you like your password to be? "))

    random.shuffle(characters)
    password = []

    for x in range(pass_lenth):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)
    print(f'Your password is {password}')    

generate_pass()    