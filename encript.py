import random

def get_prime(n):
	prime = True
	for i in range(2,n-1):
		if n % i == 0:
			prime = False
			break
	return prime

prime = False
while (prime == False):
	#p = input("INPUT THE VALUE OF P: ")
	p = random.randint(1,256)
	p=int(p)
	prime = get_prime(p)

prime = False
while (prime == False):
	#q = input("INPUT THE VALUE OF Q: ")
	q = random.randint(1,256)
	q = int(q)
	if p == q:
		print("Q MUST BE DIFFERENT FROM  P")
		prime = False
	else:
		prime = get_prime(q)

prime = False
while (prime == False):
	#e = input("INPUT THE E EXPONENT: ")
	e = random.randint(1,256)
	e = int(e)
	prime = get_prime(e)

n = p * q
phin = (p-1)*(q-1)

for i in range(1,n):
	res = i*e%phin
	if res == 1:
		print(i)
		d = i
		break

print("CLAVE PUBLICA ",str(e),str(n))
print("CLAVE PRIVADA ",str(d),str(n))