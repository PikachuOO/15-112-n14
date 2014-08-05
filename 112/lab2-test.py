#!/usr/bin/python
# dmelvin
#------------------------
def areComplementary(strand1,strand2):
	if (len(strand1) != len(strand2)):
		return False
	for i in range(len(strand1)):
		if strand1[i] not in "ATGC":
			return False
		if strand2[i] not in "ATGC":
			return False
		if strand1[i] == "A" and strand2[i] != "T":
			return False
		elif (strand1[i] == 'T' and (strand2[i] != 'A')):
			return False
		elif (strand1[i] == 'G' and (strand2[i] != 'C')):
			return False
		elif (strand1[i] == 'C' and (strand2[i] != 'G')):
			return False	
	return True
def testAreComplementary():
    print "Testing areComplementary..."
    assert(areComplementary("A", "T") == True)
    assert(areComplementary("CTAGG", "GATCC") == True)
    assert(areComplementary("CTA", "GATT") == False)
    assert(areComplementary("CTACGC", "GAT") == False)
    assert(areComplementary("GGcT", "CCGA") == False)
    print "All tests passed!"

def targetAtIndex(strand, target, i):
    targetlist = [target]
    for s in targetlist:
        if( "." in s):
            targetlist.append( s.replace(".", "A"))
            targetlist.append( s.replace(".", "T"))
            targetlist.append( s.replace(".", "G")) 
            targetlist.append( s.replace(".", "C")) 
        if ("x" in s):
            targetlist.append( s.replace("x", "A")) 
            targetlist.append( s.replace("x", "T"))
        if ("y" in s):
            targetlist.append( s.replace("y", "G")) 
            targetlist.append( s.replace("y", "C"))
    #print targetlist
    sub = strand[i: i+ len(target) ]
   # print "Substring: ", sub
    
    if (sub in targetlist):
        #print "True!"
        return True
    else:
        #print "False!"
        return False
def findTarget(strand, target):
    targetlist = [target]
    for s in targetlist:
        if( "." in s):
            targetlist.append( s.replace(".", "A"))
            targetlist.append( s.replace(".", "T"))
            targetlist.append( s.replace(".", "G")) 
            targetlist.append( s.replace(".", "C")) 
        if ("x" in s):
            targetlist.append( s.replace("x", "A")) 
            targetlist.append( s.replace("x", "T"))
        if ("y" in s):
            targetlist.append( s.replace("y", "G")) 
            targetlist.append( s.replace("y", "C"))
    #print targetlist
    for search in targetlist:
        loc = strand.find(search)
        if (loc != -1):
            #print "Index of: ", search, " in ", strand, " is ", loc
            return loc
    #print "Search not found"
    return loc #if target isn't found

def testAtIndex():
    print "Testing targetAtIndex..."
    assert(targetAtIndex("A","A",0) == True)
    assert(targetAtIndex("AAAT","AT",2) == True)
    assert(targetAtIndex("AAAT","xT",2) == True)
    assert(targetAtIndex("GCCATA","yA.",2) == True)
    assert(targetAtIndex("GCCATA","TAC",4) == False)
    print "All tests passed!"

def testFindTarget():
    print "Testing findTarget..."
    assert(findTarget("A", "A") == 0)
    assert(findTarget("ATCGGA", "GAT") == -1)
    assert(findTarget("ATACGTG","ACGT") == 2)
    assert(findTarget("TTAGTTA","xyT.") == 2)
    print "All tests passed!"

testAreComplementary()
#targetAtIndex("AAAT","xT",2)
testAtIndex()
#findTarget("A", "A")
testFindTarget()