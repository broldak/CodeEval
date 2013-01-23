def sumDigits(n):
	sum = 0
	print n
	strN = str(n)
	print strN
	for x in strN:
		print x
		sum += int(x)
		print sum


sumDigits(2**1000)