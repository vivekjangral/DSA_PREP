import math


def countDigitUsingLog(n):
    count = math.floor(math.log10(n)+1)
    return count

def count(n):
    count = 0
    while n >0:
        count +=1
        n = n//10
    return count


n=1297474

print("\n","===============================================", "\n")
print(" No of Digit in ' " + str(n) + " ' using simple count: ",count(n))
print("\n","===============================================","\n")

print("\n","===============================================", "\n")
print(" No of Digit in ' " + str(n) + " ' using simple log10: ",countDigitUsingLog(n))
print("\n","===============================================","\n")
