import string
import sys

def mthToLast(letters):
	myLetters = []
	number = 0
	for x in letters:
		if x in string.ascii_letters:
			myLetters+=x
		if x in string.digits:
			number = int(x)
	if (number <=len(myLetters) and number> 0):
		print myLetters[len(myLetters)-number]
	if (number == 0):
		print myLetters[len(myLetters)-1]


test_cases = open(sys.argv[1], 'r')
total = 0
for test in test_cases:
	if test:
		x = test[1]
		mthToLast(test)
test_cases.close()