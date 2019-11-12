maxi = input("Ingrese numero max: ")
maxi = int(maxi)

def get_prime(n):
	prime = True
	for i in range(2,n-1):
		if n % i == 0:
			prime = False
			break
	return prime


for x in range(2,maxi):
	prime = get_prime(x)
	if prime:
		print(str(x))
