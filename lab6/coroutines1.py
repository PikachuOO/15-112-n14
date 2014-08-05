#!/usr/bin/python

def capitalize():
    while True:
        value = (yield)
        print value.upper()

s = "The quick brown fox jumped over the lazy old dog."

capCo = capitalize()
capCo.next()

for word in s.split():
    capCo.send(word) #Assuming print one word on each line