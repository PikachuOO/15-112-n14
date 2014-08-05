#!/usr/bin/python
from factorial import factorial
def pascal(n):
    for i in range(n):
        for j in range(i+1):
            val = factorial(i) / (factorial(j) * (factorial(i-j)))
            print "%3d" % val,
        print "\n"
pascal(10)