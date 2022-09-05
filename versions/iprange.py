from random import seed
from random import randint

# I have no idea what i am doing lol
# im just trying to learn here

def ip_gen():
    num = randint(0, 256)
    return num

while True:
    print(f'IP: {ip_gen()}.{ip_gen()}.{ip_gen()}.{ip_gen()}')