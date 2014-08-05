out = "%3d"
x = 0
while (x < 11):
    y = 0
    while ( y < 11):
        print "%3d" % (x*y),
        y += 1
    print ""
    x+=1