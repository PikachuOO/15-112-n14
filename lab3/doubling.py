#!/usr/bin/python
def doubling(rate):
    low = float(0)
    high = float(10000)
    guess = float(5000)
    guess_error = float(5000)
    while (guess_error > 0.001):
        check = (1*(1+rate)**guess)-(2*1)
        if (check >= 0):
            high = guess
        else:
            low = guess
        guess = (high+low)/2
        guess_error = (high-low)/2
    return guess
print doubling(0.1)
print doubling(0.05)
print doubling(0.01)