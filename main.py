import random

from cryptography.fernet import Fernet
import sys
import math
import my_functions

def isPrime(N):
    for x in range(2,N):    #numbers from 2 to N-1
        if N%x == 0:
            return False
    return True


def printPrimes(M):
    for x in range(9999999,M):
        if isPrime(x):
            print(x, end=" ")

SEED_SIZE = 16
MODULUS = 36389
GENERATOR = 1500

FUNCTION_L = lambda x: x**2 - 2*x + 1


def function_H(first_half, second_half):
    mod_exp = bin(pow(GENERATOR, int(first_half, 2), MODULUS)).replace('0b', '').zfill(SEED_SIZE)
    hard_core_bit = 0
    for i in range(len(first_half)):
        hard_core_bit = (hard_core_bit ^ (int(first_half[i]) & int(second_half[i]))) % 2
    return mod_exp + second_half + str(hard_core_bit)


def function_G(initial_seed):
    binary_string = initial_seed
    result = ''
    for i in range(FUNCTION_L(SEED_SIZE)):
        first_half = binary_string[:int(len(binary_string)/2)]
        second_half = binary_string[int(len(binary_string)/2):]
        binary_string = function_H(first_half, second_half)
        result += binary_string[-1]
        binary_string = binary_string[:-1]
    return result




rsa_data = ()

def print_hi(name):
    temp_list = []
    temp_list.append(1)
    temp_list.append(2)
    temp_list.append(3)
    rsa_data = tuple(temp_list)
    print(type(rsa_data))



def change_element_in_tuple(t, i, num):
    ll = list(t)
    ll[i] = num
    t = tuple(ll)
    return t

primes = [i for i in range(4000, 8999) if my_functions.is_prime(i)]
def key_exchange(p, q, x):
    y = 0
    while y == 0 or y == 1:
        if y == 1:
            p = random.choice(primes)
            q = random.choice(primes)
            x = random.randint(10, 100)
        if not my_functions.is_prime(p) or not my_functions.is_prime(q):
            raise ValueError('P or Q were not prime')

        print("start p: " + str(p))
        print("start q: " + str(q))
        print("start x: " + str(x))
        print('')
        eq = (p - 1) * (q - 1) + 1
        y = 1
        xy = x * y
        while xy != eq:
            x += 1
            y = eq // x
            xy = x * y

    print("modulo (pq): " + str(p * q))
    print("public key, x: " + str(x))
    print("private key, y: " + str(y))
    print('****************************************')

'''
if __name__ == '__main__':

    print(primes)
    print(len(primes))

    for i in range(10):
        key_exchange(random.choice(primes), random.choice(primes),
                     random.randint(10, 100))
'''