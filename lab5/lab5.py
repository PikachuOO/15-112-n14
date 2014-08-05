#!/usr/bin/python
from readMaze import readMaze

def findStart(maze):
	for o in range(len(maze)):
		for i in range(len(maze[o])):
			if (maze[o][i] == "S"):
				return o, i

def mazeSolver(maze, row, col, sol):
	if (row > len(maze)-1 or row < 0):
		return False
	elif ( col > len(maze[row])-1 or col < 0 ):
		return False
	elif (maze[row][col] == "W"):
		return False
	elif (maze[row][col] == "F"):
		return True
	
	maze[row][col] = "W"
	
	if ( mazeSolver(maze,row-1,col, sol) or #up
		mazeSolver(maze,row,col+1, sol) or  #right
		mazeSolver(maze,row,col-1, sol) or  #left
		mazeSolver(maze,row+1,col, sol)     #down
	):
		sol.append( (row, col))
		return True
	else:
		return False
	
mazeFile = "2.txt"
maze = []  # This declares the maze as an empty list
workingSol = []

readMaze(maze, mazeFile) # This reads the maze into the list
startRow, startCol = findStart(maze)

if( mazeSolver(maze, startRow, startCol, workingSol) ):
	mazeSolution = list(reversed(workingSol))
	print "===Solution coordinates===="
	print mazeSolution
else:
	print "No solution found."