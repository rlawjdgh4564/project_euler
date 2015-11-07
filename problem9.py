for a in range(1, 1001):
	for b in range(1, 1001):
		c = a**2 + b**2
		if a+b+c**0.5 == 1000:
			print int(a*b*(c**0.5))
			break;
	
