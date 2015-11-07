def fibo(n):
	if n == 1 or n == 2:
		return 1
	elif n > 2:
		return fibo(n-1) + fibo(n-2)
	else:	return False
sum_ = 0
i = 0
while True:
	i += 1
	if fibo(i) > 4000000:	break
	if fibo(i) % 2 == 0:	sum_ += fibo(i)

print sum_
