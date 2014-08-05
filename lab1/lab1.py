#!/user/bin/python
def part1():
    print "PART 1: Prompt the user for their name and print the name"
    name = raw_input("What is your name? ")
    print "Thanks, " + name
def part2():
    print "\nPART 2: Prompt for two numbers, print both numbers on the same line"
    num1 = int(raw_input("Enter number one: "))
    num2 = int(raw_input("Enter number two: "))
    print "You inputted: ",
    print num1,
    print num2
def part3():
    print "\nPART 3: Use a loop to print out the numbers from 1 through 10, inclusive"
    num = 1
    while (num <= 10):
        print num
        num += 1
def part4():
    print "\nPART 4: Greatest Absolute Value"
    num1 = abs(float(raw_input("Enter number 1: ")))
    num2 = abs(float(raw_input("Enter number 2: ")))
    if (num1 < num2):
        print "Greater absolute value: ",
        print num2
    elif (num1 > num2):
        print "Greater absolute value: ",
        print num1
    else:
        "Tie"
def greater(num1, num2):
    if (num1 < num2):
        return num2
    elif (num1 > num2):
        return num1
    else:
        return 0
def less(num1, num2):
    if (num1 < num2):
        return num1
    elif (num1 > num2):
        return num2
    else:
        return 0 
def part5():
    print "\nPART 5: Inclusive average"
    num1 = int(raw_input("Enter number 1: "))
    num2 = int(raw_input("Enter number 2: "))
    stop = greater(num1, num2)
    count = less(num1, num2)
    add = 0
    while (count <= stop):
        add += count
        count += 1
    print "Average: ",
    print add/(stop-less(num1, num2)+1) #integer division
def part6():
    print "\nPART 6: Times Table 0-10"
    for x in range (0, 11):
        for y in range (0, 11):
            print x*y,
        print "\n"
part1()
part2()
part3()
part4()
part5()
part6()