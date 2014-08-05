#!/usr/bin/python
#assrt nonnegative height?
def triangle (height):
   
    for o in range (1, height+1):
        i = o
        for i in range (i, height):
            print " ",
        for x in range (1, 2*o ):
            print "*",
        print "\n"
triangle(3)
triangle(5)