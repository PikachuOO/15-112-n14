class NegativeError(Exception):
    def __init___(self, value):
        self.value = value
    def __str__ (self):
        return repr(self.value)
def divide(x,y):
    try:
        if (x < 0 or y < 0):
            raise NegativeError("One of the numbers was negative")
        return x/y
        '''
    except (ZeroDivisionError) as r:
        print "omg", type(r)
    except TypeError as e:

        print "wow ", type(e)
        '''
    except  (ZeroDivisionError,TypeError, NegativeError) as x:
        print type(x), repr(x)
        print "This is before I reraise!"
        #raise x

print divide(10,2)
print divide(1,2)
print divide(1,0)
print divide(1,"f")
print divide(1,-1)