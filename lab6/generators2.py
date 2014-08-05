#!/usr/bin/python

def wordsFromFile(filename):
    textfile = open(filename, "r")
    lines = textfile.readlines() #assuming words are line separated
   
    wordsNested = [[word for word in line.split()] for line in lines]
    wordsFlat = [word for innerList in wordsNested for word in innerList]
    #for each innerList in wordsNested, append each word in that innerList
   
    for word in wordsFlat:
        yield word

def noPunctuation(wordGenerator):
    for word in wordGenerator:
        word = word.replace(",", "")
        word = word.replace(".", "")
        word = word.replace("-", "")
        word = word.replace(":", "")
        word = word.replace(";", "")
        word = word.replace("\n", "")
        word = word.replace("\"", "")

        yield word
def allCaps(wordGenerator):
    for word in wordGenerator:
        yield word.upper()

wordGen = wordsFromFile("wordsFromFile.txt")
noPunGen = noPunctuation(wordGen)
capsGen = allCaps(noPunGen)

wordSet = set([])
for word in capsGen:
    wordSet.add(word)

print wordSet