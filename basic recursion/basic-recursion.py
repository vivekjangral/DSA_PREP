# Print a word n times using recursion
def printNTimesWord(name, totalPrint):
    if totalPrint == 0:
        return
    print("  " + name)
    printNTimesWord(name, totalPrint - 1)

def printNTimesDigit(count, totalCount):
    if count > totalCount:
        return
    print(count)
    printNTimesDigit(count + 1, totalCount)


def printNTimesDigitReverse(count, totalCount):
    if count < 1:
        return
    print(count)
    printNTimesDigitReverse(count - 1, totalCount)


name = "Hello World"
totalPrint = 5
count = 1
totalCount = 5

print("\n","===============================================", "\n")
print(" Printing word " + str(totalPrint) + " times\n")
printNTimesWord(name, totalPrint)
print("\n","===============================================","\n")


print(" Printing from " + str(count) +" to " + str(totalCount) +"\n")
printNTimesDigit(count, totalCount)
print("\n","===============================================","\n")


print(" Printing from " + str(totalCount) +" to " + str(count) +"\n")
printNTimesDigitReverse(totalCount, totalCount)
print("\n","===============================================","\n")



