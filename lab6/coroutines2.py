#!/usr/bin/python

def wordsFromFile(filename):
    textfile = open(filename, "r")
    lines = textfile.readlines() #assuming words are line separated
   
    wordsNested = [[word for word in line.split()] for line in lines]
    wordsFlat = [word for innerList in wordsNested for word in innerList]
    #for each innerList in wordsNested, append each word in that innerList
   
    for word in wordsFlat:
        yield word

def noPunctuation(nextCo):
    while True:
        word = (yield)
        word = word.replace(",", "")
        word = word.replace(".", "")
        word = word.replace("-", "")
        word = word.replace(":", "")
        word = word.replace(";", "")
        word = word.replace("\n", "")
        word = word.replace("\"", "")

        nextCo.send(word)

def allCaps(nextCo):
    while True:
        word = (yield)
        nextCo.send(word.upper())

def setWords(wordSet):
    while True:
        word = (yield)
        wordSet.add(word)

wordSet = set ([])

setCo = setWords(wordSet)
setCo.next()
capsCo = allCaps(setCo)
capsCo.next()
noPunCo = noPunctuation(capsCo)
noPunCo.next()
wordGen = wordsFromFile("wordsFromFile.txt")

for word in wordGen:
    noPunCo.send(word)

print wordSet