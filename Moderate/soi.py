import string
import sys

def pangram(sentence):
	myAlphabet = string.ascii_lowercase
	for x in sentence:
		if x in string.ascii_lowercase:
			myAlphabet = myAlphabet.replace(x, "")
	if len(myAlphabet)>0:
		print myAlphabet
	else:
		print "NULL"


sum = 0
test_cases = open(sys.argv[1], 'r')
total = 0
for test in test_cases:
	if test:
		pangram(test)
test_cases.close()
    