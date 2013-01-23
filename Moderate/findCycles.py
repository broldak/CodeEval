import itertools
def findCycles(numbers):
	newArray = numbers.split(" ")
	print newArray

	print set(itertools.combinations(newArray, 2))
	for x in set(itertools.combinations(newArray, 2)):
		for y in x:
			print y

findCycles("1 2 3 2 3")