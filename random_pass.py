import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
number = 1
length = 8

for pwd in range(number):
    passwords = ''
    for pwd in range(length):
        passwords += random.choice(chars)
    print(passwords)
