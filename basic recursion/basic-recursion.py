# Print a word n times using recursion
def printNTimesWord(name, totalPrint):
    if totalPrint == 0:
        return
    print("  " + name)
    printNTimesWord(name, totalPrint - 1)

def printNTimesDigit(count, totalCount):
    if count < totalCount:
        return
    print("  " + str(count))
    printNTimesDigit(count +1, totalCount)

name = "Hello World"
totalPrint = 5
count = 0
totalCount = 5

print("\n","===============================================", "\n")
print(" Printing word " + str(totalPrint) + " times\n")
printNTimesWord(name, totalPrint)
print("\n","===============================================","\n")

print("\n","===============================================", "\n")
print(" Printing from " + str(count) +" to " + str(totalCount) +"\n")
printNTimesDigit(count, totalCount)
print("\n","===============================================","\n")



