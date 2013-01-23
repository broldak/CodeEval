import string
import sys

def primeLessN(number):
	primes = ""
	for x in xrange(1, number):
		if(isPrime(x)):
			primes+=str(x) + ","
	print primes[0:len(primes)-1]

def isPrime(number):
	if number<2:
		return False
	if number == 2:
		return True
	if number%2 == 0:
		return False
	for i in xrange(2, int(round(number**0.5))+1):
		if (number%i == 0):
			return False
	return True

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	if test:
		test = int(test)
    	primeLessN(test)

test_cases.close()