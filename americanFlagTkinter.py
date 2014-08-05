#!/usr/bin/python

from Tkinter import *
root = Tk()

def drawAmericanFlag(canvas, x0, y0, x1, y1, stripeheight, cheight, cwidth):
	#width = x1-x0
	for x in range(13):
		if (x % 2 == 0):
			canvas.create_rectangle(x0, y0+(x*stripeheight), x1, y1*(x+1), fill="red")
		else:	
			canvas.create_rectangle(x0, y0+(x*stripeheight), x1, y1*(x+1), fill="white")
	canvas.create_rectangle(0,0, .76/cheight, .5385/cheight, fill="blue")

canvas = Canvas(root, width = 300, height = 200)
canvas.pack()
cwidth = canvas.cget("width")
stripeheight = int(canvas.cget("height"))/13
cheight = int(canvas.cget("height"))

drawAmericanFlag(canvas, 0, 0, cwidth, stripeheight, stripeheight, cheight, cwidth)


root.mainloop()