from prime import isPrime

num = 600851475143
sol = 0
i = num
while i > 0:
	i -= 1
	if num % i == 0:
		if isPrime(i):
			sol = i
print sol
