def runningTotal():
    sum = 0
    while True:
        val = (yield)
        sum += val
        print sum
x = runningTotal()
x.next()
for y in range(10):
    x.send(y)