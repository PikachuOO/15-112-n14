def printWord():
    while True:
        word = (yield)
        print word

def noPeriod(target):
    while True:
        word = (yield)
        target.send(word.replace(".",""))

def up(target):
    while True:
        word = (yield)
        target.send(word.upper())

def numGen(target):
    num = 1
    while True:
        word = (yield)
        target.send( "%02d" % num + ": " + word )
        num += 1
pw = printWord()
pw.next()
np = noPeriod(pw)
next(np)
up = up(np)
up.next()
num = numGen(up)
num.next()

for word in "I like to eat. Particularly, I like to eat apples and bananas.".split():
    num.send(word)