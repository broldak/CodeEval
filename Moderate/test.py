import sys
import string

def findDuplicate(numbers):
	semi = string.find(numbers, ";")
	numbers = numbers[semi+1:]
	newList = [int(x) for x in numbers.split(',')]
	print newList

findDuplicate('5;4,3,20,1,20')