#!/usr/bin/python

def generateMultiples(number, start):
    while start < 81:
        yield start #should 17 print first?
        start += number

gen = generateMultiples(3, 27)

for x in range( 18):
    print gen.next()