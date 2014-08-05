#!/usr/bin/python
def num_occurrences(list, key):
    count = 0
    for x in list:
        if (x == key):
            count += 1
    return count
print num_occurrences(["a", "b", "a", "b", "c", "b", "d", "e"], "b")