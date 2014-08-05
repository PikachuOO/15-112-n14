class NegativeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
sum = 0
while (True):
    try:
        num = int(raw_input("Enter number: "))
    
    except ValueError as ve:
        print "Testing..."
        print ve
        #raise ve
        break
    if (num < 0):
        raise NegativeError("Number less than 0")
    sum += num
new = "Result: %d" % sum
print new