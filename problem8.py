f = open("input.txt", "r")

sum_ = 1
max_ = 0
while True:
	line = f.readline()
	if not line: break
	for i in range(0, 46):
		token = line[i: i+5]
		for x in token:
			sum_ *= int(x)
		if sum_ > max_: max_ = sum_
		sum_ = 1
print max_
f.close()
