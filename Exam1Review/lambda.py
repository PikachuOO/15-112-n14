foo = range(1, 101)
for i in range(2, 11):
    foo = filter(lambda x: x % i or x == i , foo)
print foo