#!/usr/bin/python

from Tkinter import *
from random import randint
import tkMessageBox

def timerFired():
    if not c.d.isGameOver:
        if (moveFallingPiece(1,0) == False):
            placeFallingPiece()
            newFallingPiece()
            if (fallingPieceIsLegal() == False):
                c.d.isGameOver = True
                tkMessageBox.showinfo("Game Over!", "Press r to restart.")
               
    redrawAll()
    delay = 400 # milliseconds
    c.after(delay, timerFired)

def initPieces():
    iPiece = [
    [ True,  True,  True,  True]
    ]

    jPiece = [
    [ True, False, False ],
    [ True, True,  True]
    ]

    lPiece = [
    [ False, False, True],
    [ True,  True,  True]
    ]

    oPiece = [
    [ True, True],
    [ True, True]
    ]

    sPiece = [
    [ False, True, True],
    [ True,  True, False ]
    ]

    tPiece = [
    [ False, True, False ],
    [ True,  True, True]
    ]

    zPiece = [
    [ True,  True, False ],
    [ False, True, True]
    ]

    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]
  
    c.d.pieces = tetrisPieces
    c.d.pieceColors = tetrisPieceColors

def fallingPieceCenter():
    row = c.d.fallingPieceRow+( len(c.d.fallingPiece)/2 )
    col = c.d.fallingPieceCol+(len(c.d.fallingPiece[0])/2)
    return (row, col)

def rotateCounterClockwise(l):
    newList = []

    rows = len(l)
    
    cols = len(l[0])
    y = -1
    x = 0

    for col in range(cols):
        newRow = []
        x = 0
        for row in range(rows):
            
            newRow.append(l[x][y])
            x += 1
        newList.append(newRow)
        y -= 1

    return newList

def rotateFallingPiece():
    
    oldPiece = c.d.fallingPiece
    oldPieceRow = c.d.fallingPieceRow
    oldPieceCol = c.d.fallingPieceCol
        
    (oldCenterRow, oldCenterCol) = fallingPieceCenter()
    
    
    c.d.fallingPiece = rotateCounterClockwise(c.d.fallingPiece)
    
    (newCenterRow, newCenterCol) = fallingPieceCenter()


    c.d.fallingPieceRow += (oldCenterRow - newCenterRow)
    c.d.fallingPieceCol += (oldCenterCol - newCenterCol)
    

    if (fallingPieceIsLegal() == False):
        c.d.fallingPiece = oldPiece
        c.d.fallingPieceRow = oldPieceRow
        c.d.fallingPieceCol = oldPieceCol
        

    drawFallingPiece()
    
def init():
    c.d.board = []
    c.d.score = 0
    for x in range(c.d.rows):
        c.d.board+= [[c.d.emptyColor]*c.d.cols]

    initPieces()
    newFallingPiece()
    c.d.isGameOver = False 

def removeFullRows():
    c.d.fullRows = 0
    
    newRow = []
    for y in reversed( range(len(c.d.board)) ):
        if c.d.board[y].count(c.d.emptyColor) != 0:
            newRow = [c.d.board[y]] + newRow
        else:
            c.d.fullRows += 1

    for row in range(c.d.fullRows):
        newRow = [[c.d.emptyColor for col in range(c.d.cols)]] + newRow

    c.d.board = newRow 
    c.d.score += c.d.fullRows**2
    

def redrawAll():
    c.delete(ALL)
    
    drawGame()
    drawScore()

def drawScore():
    c.create_text(20, 20, text="Score: %d" % c.d.score, anchor="nw")
    
def drawGame():
    c.create_rectangle(0,0,c.d.cwidth, c.d.cheight, fill=c.d.bgcolor, width=0)
    
    removeFullRows()
    drawBoad()
    drawFallingPiece()
    
def drawBoad():
    for x in range(c.d.rows):
        for y in range(c.d.cols):  
            drawCell(x,y,c.d.board[x][y])

def drawCell(row, col, color):
    c.create_rectangle(  25+(40*col),   45+(40*row), 65+(40*col), 85+(40*row), fill="black")
    c.create_rectangle(  25+(40*col),   45+(40*row), 65+(40*col), 85+(40*row), fill=color)

def newFallingPiece():
    c.d.fallingPiece = c.d.pieces[randint(0, 6)]
    c.d.fallingPieceColor = c.d.pieceColors[randint(0, 6)]
    c.d.fallingPieceRow = 0
    fallingPieceCols = len(c.d.fallingPiece[0]) 
    c.d.fallingPieceCol = c.d.cols/2 - fallingPieceCols/2
    c.d.pieceWidth = len(c.d.fallingPiece[0])
    c.d.pieceHeight = len(c.d.fallingPiece)

    drawFallingPiece() 

def drawFallingPiece():    
    for y in range( len(c.d.fallingPiece) ):
        for x in range(len(c.d.fallingPiece[0])):
            if (c.d.fallingPiece[y][x]):
                drawCell(c.d.fallingPieceRow +y,c.d.fallingPieceCol+x,c.d.fallingPieceColor)

def keyPressed(event):
    key = event.keysym
    if (key == "r"):
        init()
    if c.d.isGameOver == False:
        if (key == "Left"):
             moveFallingPiece(0, -1)
        elif (key == "Down"):
            moveFallingPiece(1, 0)
        elif (key == "Right"):
            moveFallingPiece(0, 1)
        elif (key == "Up"):
            rotateFallingPiece()
    redrawAll()

def moveFallingPiece(drow, dcol):
    c.d.fallingPieceRow += drow
    c.d.fallingPieceCol += dcol
    

    if (fallingPieceIsLegal() == False):
        c.d.fallingPieceRow -= drow
        c.d.fallingPieceCol -= dcol
        return False
    else:
        return True

def placeFallingPiece():
    for y in range( len(c.d.fallingPiece) ):
        for x in range(len(c.d.fallingPiece[0])):
            if (c.d.fallingPiece[y][x]):
                c.d.board[y+c.d.fallingPieceRow][x+c.d.fallingPieceCol] = c.d.fallingPieceColor

def fallingPieceIsLegal():
    #return True
    for y in range( len(c.d.fallingPiece) ):
        for x in range(len(c.d.fallingPiece[0])):
            if(c.d.fallingPiece[y][x]):
                if (c.d.fallingPieceRow+y >= c.d.rows):
                    return False
                if (c.d.fallingPieceRow+y < 0):
                    return False
                if (c.d.fallingPieceCol+x < 0):
                    return False
                if (c.d.fallingPieceCol+x >= c.d.cols):
                    return False
                if (c.d.board[c.d.fallingPieceRow+y][c.d.fallingPieceCol+x] != c.d.emptyColor):
                    return False
    return True

def run(rows, cols):
    cwidth = cols*40 + 50
    cheight = rows*40 + 50

    root = Tk()
    global c
    c = Canvas(root, width=cwidth, height=cheight)
    c.pack()
    root.resizable(width=0, height=0)
    class Struct:
        pass
    c.d = Struct()


    c.d.rows = rows
    c.d.cols = cols
    c.d.board = []
    c.d.emptyColor = "blue"
    c.d.bgcolor = "darkgray"
    c.d.cwidth = c.cget("width")
    c.d.cheight = c.cget("height")

    init()
    timerFired()
    root.bind("<Key>", keyPressed)
    root.mainloop()
    
run(15, 10)