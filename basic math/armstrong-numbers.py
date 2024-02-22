
def isArmstromgNumber(n):
    temp = n
    sum = 0
    while n >0:
        lastNumber = n % 10
        n = n//10
        sum = sum + (lastNumber **3)
    return temp == sum


n=371

print("\n","===============================================", "\n")
print(" Is Number ' " + str(n) + " ' is armstrong number  : ",isArmstromgNumber(n))
print("\n","===============================================","\n")

