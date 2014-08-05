#!/usr/bin/python
from random import randint

wordsFile = open("words5.txt")
wordsListOriginal = wordsFile.readlines()
wordsList = [word.rstrip('\n') for word in wordsListOriginal]

words = {}
for word in wordsList:    
    words[word] = [0]

rand = randint (0, 2415)
target = wordsList[rand]
print rand, target

guess = raw_input().lower()
guessLetters = list(guess)
targetLetters = list(target)

if len(guessLetters) != 5:
    print "Guesses must be 5 letter words"
if guessLetters[0] != targetLetters[0]:
    print "Guesses must start with the correct letter"
#check for numbers, punctuation, symbols, etc.
#check if word is in dictionary

guessEnum = list(enumerate(guess))
targetEnum = list(enumerate(target))

goodPos = []
goodLet = []

# for it, gt in map(None, guessEnum, targetEnum):
#     if ( it[1] == gt[1] ):
#         goodPos.append(it[0])

for i, g in guessEnum:
    print "i: ", i
    print "g: ", g
    pos = target.find(g)
    print "pos: ", pos

    if (pos == i):
        print "Match letter and pos"
        goodPos.append(pos)
    elif (pos != -1):
        print "Match letter"
        goodLet.append(pos)

    

print "goodPos: ", goodPos
print "goodLet: ", goodLet
#print guessLetters
#print targetLetters