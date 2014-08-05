g = lambda x: x +1
print g(10)

def num(n):
    return lambda x: x + n

h = num(3)
print h(3)