sum_ = 0
sum_2 = 0
for i in range(1, 101):
	sum_ += i**2
	sum_2 += i
sum_2 = sum_2 ** 2

print sum_2 - sum_
