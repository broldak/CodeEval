import math
import string
def spiralPrint(matrix):
	rows = matrix[:1]
	cols = matrix[2:3]
	straightList = [int(x) for x in matrix[4:].split(" ")]
	print straightList
	constructMatrix(straightList, int(rows), int(cols))


def constructMatrix(straightList, rows, cols):
	length = len(straightList)
	increment = rows
	newMatrix = []
	for x in xrange(rows):
		newMatrix+=[straightList[x]]
	count = 1
	for x in xrange(increment, increment+cols-1):
		print straightList[7],(rows-1)*count+x
		newMatrix+=[straightList[(rows-1)*count+x]]
		print newMatrix
		count+=1
	count = 1
	print increment+cols, increment+cols+rows-1
	for x in xrange(increment+cols, increment+cols+rows-1):
		newMatrix+= [straightList[(length-1)-count]]
		print newMatrix
		count+=1

spiralPrint("3;6;1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18")