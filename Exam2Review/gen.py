import random

def rand(min, max):
    while True:
        yield (random.randint(min, max))
def half(randInput):
    while True:
        yield randInput.next()/2
def cube(halfInput):
    while True:
        yield halfInput.next()**3

r = rand(1, 100)
halfnum = half(r)
cubed = cube(halfnum)

for x in range(10):
    print r.next(), halfnum.next(), cubed.next()