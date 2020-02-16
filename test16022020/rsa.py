'''
620031587
Net-Centric Computing Assignment
Part A - RSA Encryption
'''
import random

def suma(a,b):
    return a+b, a-b, a*b,a%b

print(suma(10,20))
print(suma(20,20))
print(suma(30,20))
print(suma(40,20))

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(36,256))

print(gcd(21,78))


print(gcd(170, 750))


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    for i in range(1,phi):
        res = e * i % phi
        print("RES",res,e,i,phi)
        if res == 1:
            return i
print(multiplicative_inverse(127, 211))

'''
Tests to see if a number is prime.
'''
def is_prime(num):
    prime = True
    if num == 2:
        return False
    if num < 2 or num % 2 == 0:
        return False
    for i in range(2, num-1):
        print("I",  i, num)
        if num % i == 0:
            prime = False
            break
    return prime
print("127",is_prime(127))
print("******")
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        print(n,num)
        if num % n == 0:
            return False
    return True

print("127",is_prime(127))
