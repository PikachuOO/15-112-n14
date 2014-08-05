#!/usr/bin/python

l = [[1,2], [3,4], [5,6]]
l2 = [[ 1,  2,  3,  4]]
l3 = [[1], [2], [3], [4]]
def rotateCounterClockwise(l):
	newList = []

	if (len(l) == 4):
		rows = 1
		cols = 4
	else:
		rows = len(l)
		cols = len(l[0])
	
	#print "Cols: ", cols
	print "Rows: ", rows
		
	for x in reversed(range(cols)):
		row = []
		for y in range(rows):
			#print x, y, l[y][x]
			
			row.append(l[y][x])
		newList.append(row)

	#print "len of newList: ", len(newList)
	print newList
	return newList
def test(l):
	rotated =  zip(*l)[::-1]
	return rotated

def rotate(l):
	newList = []

	rows = len(l)
	print "rows: ", rows
	print "range of rows: ", range(rows)
	cols = len(l[0])
	y = -1
	x = 0

	for col in range(cols):
		newRow = []
		x = 0
		for row in range(rows):
			#print "row in for loop: ", row
			#print x
			newRow.append(l[x][y])
			x += 1
		newList.append(newRow)
		y -= 1

	print newList

rotate(l)
rotate(l2)
rotate(l3)

#rotateCounterClockwise(l)
#rotateCounterClockwise(l2)
#rotateCounterClockwise(l3)
#test(l)
#assert(rotateCounterClockwise(l) == [[2,4,6],[1,3,5]])
#assert(test(l) == [(2,4,6),(1,3,5)])