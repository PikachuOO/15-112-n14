class NegativeAmountError(Exception):
    def __init__ (self, value):
        self.value = value
    def __str__ (self):
        return repr(self.value)

def  creditChecking(amount):
    bal = 0
    if (amount < 0):
        raise NegativeAmountError("Amount must be negative")
    else:
        bal += amount
        print bal
try:
    creditChecking(5)
    creditChecking(-5)
except NegativeAmountError as n:
    print "Amount must be non-negative"
    raise n