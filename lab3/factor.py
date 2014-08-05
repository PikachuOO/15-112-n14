#!/usr/bin/python

def factor(n):
    dividend = n
    possible_factor = 2
    factors = []
    while (dividend != 1):
        if (dividend % possible_factor == 0):
            factors.append(possible_factor)
            dividend /= possible_factor
        else:
            possible_factor += 1
    return factors
print factor(60)
print factor(45)
print factor(35)
print factor(13)