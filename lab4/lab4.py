#!/usr/bin/python

class NoResultsError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def readBook(line): 
    infoTuple = tuple(word.upper() for word in line.split(","))
    return infoTuple

def readBooks(fileName):
    bookFile = open(fileName) #add exception where book doesn't exist
    
    books = bookFile.readlines()
    
    bookList = [readBook(book) for book in books if book != "\n"]

    return bookList

def listTitles(bookList):
    titlesList = [item[2] for item in bookList]

    return titlesList

def buildIndex(bookList):
    titlesList =  listTitles(bookList) #convert all titles to uppercase, remove punctuation

    keyList = []
    
    wordsList = []
    for title in titlesList:
        wordsList.extend(title.split())
    for word in wordsList:
        if (word != "A" and word != "AN" and word != "THE"):
                keyList.append(word)

    bookDict = {}
    for key in keyList:
        bookDict[key] = set() #will this leave empty lists with no book matches?
    count = 0
    while (count < len(titlesList)):
        for key in keyList:
            if (key in titlesList[count].split()):
                bookDict[key].add(titlesList[count])
                
        count += 1
    
    return bookDict
    
def lookupKeyword(bookDict):
    check = raw_input("Enter a key to search for: ").upper()
    if (check == ""):
        raise NoResultsError("No match found")
    checkList = check.split()
    bookList = readBooks("books.txt")
    matchDict = {}
    titlesList =  listTitles(bookList)
    
    
    for term in checkList:
        
        for key in bookDict:
            if (term == key):

                for title in bookDict[term]:
                    
                    if (title in matchDict):
                        matchDict[title] += 1
                    else:
                        matchDict[title] = 1       
        if (len(matchDict) == 0):
            raise NoResultsError("No match found")
   
    actualMatches = {}
    for key in matchDict:
       if (matchDict[key] > 0):
            actualMatches[key] = matchDict[key]
    
    matchTupleList = []
    for key in actualMatches:
        matchTupleList.append( (actualMatches[key], key) )
    matchTupleList.sort(reverse=True)

    print "\nSearch results (number of matches on left):\n"
    for item in matchTupleList:
        print item[0], item[1]

def presentMenuAndGetChoice():
    choice = ""
    while (choice != "E"):
        print "=========================="
        print "What do you want to do?"
        print "\tI)nitialize an index, Q)uery an index, or E)xit"
        choice = raw_input().upper()
        
        if (choice == "I"):
            filename = raw_input("Enter a file name (with .txt extension): ").lower()
            try:
                listOfTuples = readBooks(filename)
            except:
                print "Bad input: File not found."
                continue
            print "Index of " + filename + " generated!"
       
        if (choice == "Q"):
            
            try:
                bookDict = buildIndex(listOfTuples)
            except:
                print "Please build and index before searching it."
                continue
            
            try:
                lookupKeyword(bookDict)
            except:
                print "Key not found."
        if (choice == "E"):
            break
        
        elif(choice != "I" and choice != "Q"):
            print "Use one of the listed choices."        
    print "Goodbye."
        
presentMenuAndGetChoice()