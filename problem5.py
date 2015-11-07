from prime import isPrime

sum_ = 1

for x in range(2, 21):
	if isPrime(x):
		sum_ *= x
for x in range(2, 5):
	for y in range(2, ):
		if x ** y < 20:
			max_y = y
	sum_ *= x ** max_y
print sum_
