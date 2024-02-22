from math import sqrt

def printDivisor(n):
    divisor=[]
    i = 1
    while i * i <= n:
        if n % i == 0:
              divisor.append(i)
              if i != n // i:
                  divisor.append(n // i)
        i += 1
    return sorted(divisor)

def printAllDivisor(n):
    divisor=[]
    for i in range(1,n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor


n=36

print("\n","===============================================", "\n")
print(" All Divisor of ' " + str(n) + " ' is : \n \n",printAllDivisor(n))
print("\n","===============================================","\n")

print("\n","===============================================", "\n")
print(" All Divisor of ' " + str(n) + " ' is : \n \n",printDivisor(n))
print("\n","===============================================","\n")

