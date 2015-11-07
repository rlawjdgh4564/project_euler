from prime import isPrime

count = 0
i = 1
while True:
	i += 1
	if isPrime(i):	count += 1
	if count == 10001:
		print i
		break
