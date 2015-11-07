from prime import isPrime

sum_ = 0

for x in range(2, 2000001):
	if isPrime(x):
		sum_ += x

print sum_

