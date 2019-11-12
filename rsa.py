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

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):

    for i in range(1,phi):
        res = e * i % phi
        if res == 1:
            return i
print(multiplicative_inverse(11,96))

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
        if num % i == 0:
            prime = False
            break
    return prime
print(is_prime(17))
print(is_prime(33))
print(is_prime(17))
print(is_prime(29))

'''
for i in range(48415148782398,1,-1):
    p = is_prime(i)
    if p:
        print(i)
        break
'''

'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

'''
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

print(generate_keypair(19,29))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    #cipher = [(ord(char) ** key) % n for char in plaintext]
    chipher = [pow(ord(char),key,n) for char in plaintext]
    #Return the array of bytes
    return chipher

print(encrypt((257,551),'JOSIAS'))
print(encrypt((257,551),'FERNANDO'))

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    #plain = [chr((char ** key) % n) for char in ciphertext]
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("RSA Encrypter/ Decrypter")
    prime = False
    while prime == False:
        p = int(input("Enter a prime number (17, 19, 23, etc): "))
        prime = is_prime(p)
    prime = False
    while prime == False:
        q = int(input("Enter another prime number (Not one you entered above): "))
        if p == q:
            print("p can not be equal to q")
            prime =False
            continue
        prime = is_prime(q)
    print ("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print ("Your public key is ", public ," and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print ("Your encrypted message is: ")
    print (''.join(map(lambda x: str(x), encrypted_msg)))
    print ("Decrypting message with public key ", public ," . . .")
    print ("Your message is:")
    print (decrypt(public, encrypted_msg))