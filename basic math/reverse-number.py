
def reverseNumber(n):
    revserse = 0
    isNegative = False
    if n < 0:
        n = n * -1
        isNegative = True
    while n > 0:
        lastNumber = n % 10
        n = n//10
        revserse = (revserse * 10) + lastNumber
    return revserse * -1 if isNegative else revserse


n=1297474

print("\n","===============================================", "\n")
print(" Reverse of a  Number ' " + str(n) + " ' is : ",reverseNumber(n))
print("\n","===============================================","\n")

