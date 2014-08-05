#!/usr/bin/python

def add(x, y):
	return x + y

def nonNegative(toDec):
	def inner(*args):
		for i in args:
			if (i < 0):
				raise ValueError("Must be non-negative")
		return toDec(*args)
	return inner

def printWords(wordsList):
	for word in wordsList:
		print word

def allCaps(toDec):
	def inner(*args):
		upperStrings = []
		for word in args:
			upperStrings.append( word.upper() )
		return toDec(upperStrings)
	return inner

decorated2 = allCaps(printWords)
print "allCaps Decorator:"
decorated2("Instantiate each", "of these three generators.", "A string")

print "==============="

decorated1 = nonNegative(add)
print "Non-negative: ", decorated1(9, 3)
print "Negative: ", decorated1(3, -3)