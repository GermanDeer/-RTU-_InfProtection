import random
import math
from random import randint

class DH(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
    def generate_partial_key(self):
        partial_key = self.public_key1**self.private_key
        partial_key = partial_key%self.public_key2
        return partial_key
    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r**self.private_key
        full_key = full_key%self.public_key2
        self.full_key = full_key
        return full_key


def get_prime_number():
    while True:
        number = random.randint(100, 1000000)
        if isPrime(number, 6) is True: return number

#(x^y) % p
def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p
    return res

def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if (x == 1 or x == n - 1):
        return True
    while (d != n - 1):
        x = (x * x) % n
        d *= 2
        if (x == 1):
            return False
        if (x == n - 1):
            return True
    return False

def isPrime(n, k):
    # Corner cases
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2

    for i in range(k):
        if (miillerTest(d, n) == False):
            return False

    return True

k = 9

a_public = get_prime_number()
a_private = get_prime_number()
b_public = get_prime_number()
b_private = get_prime_number()
e_private = get_prime_number()

Alice = DH(a_public, b_public, a_private)
Bob = DH(a_public, b_public, b_private)
Eve = DH(a_public, b_public, e_private)

a_partial = Alice.generate_partial_key()
b_partial = Bob.generate_partial_key()
e_partial = Eve.generate_partial_key()
a_full = Alice.generate_full_key(b_partial)
b_full = Bob.generate_full_key(a_partial)
e_full = Eve.generate_full_key(a_partial)

print(f'АЛИСА\n\t* публичный: {str(a_public)}\n\t* приватный: {str(a_private)}\n\t* частичный: {str(a_partial)}\n\t* полный: {str(a_full)}')
print(f'БОБ\n\t* публичный: {str(b_public)}\n\t* приватный: {str(b_private)}\n\t* частичный: {str(b_partial)}\n\t* полный: {str(b_full)}')
print(f'ЕВА\n\t* приватный: {str(e_private)}\n\t* частичный: {str(e_partial)}\n\t* полный: {str(e_full)}')