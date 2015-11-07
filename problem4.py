save = 0
for x in range(100, 1000):
	for y in range(100, 1000):
		temp = x * y
		if str(temp) == str(temp)[::-1]:
			if save < temp:	save = temp

print save
