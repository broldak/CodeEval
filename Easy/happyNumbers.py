import sys

def sumOfSquaresOfDigits(x):
    if (x>0):
        total = (x%10)**2
        while (x/10 > 0):
            x /= 10
            total+=(x%10)**2
    elif (x<0):
        return False
    else:
        return 0
    return total

def isHappyNumber(number):
	if (number>0):
		x = number
		while(x/10>0):
			x = sumOfSquaresOfDigits(x)
		if (x == 1):
			print 1
			return True
		elif(x==7):
			print 1
			return True
		else:
			print 0
			return False
	print 0
	return False

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	if test:
		test = int(test)
    	isHappyNumber(test)

test_cases.close()
