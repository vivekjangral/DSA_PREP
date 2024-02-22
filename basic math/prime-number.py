from math import sqrt

def isPrimeNumberB(n):
    counter=0
    i = 1
    while i * i <= n:
        if n % i == 0:
              counter +=1
              if i != n // i:
                  counter +=1
        i += 1
    return True if counter==2 else False

def isPrimeNumber(n):
    counter=0
    for i in range(1,n+1):
        if n % i == 0:
           counter +=1
    return True if counter==2 else False


n=11

print("\n","===============================================", "\n")
print(" Is Number ' " + str(n) + " ' is prime number : ",isPrimeNumber(n))
print("\n","===============================================","\n")

print("\n","===============================================", "\n")
print(" Is Number ' " + str(n) + " ' is prime number : ",isPrimeNumberB(n))
print("\n","===============================================","\n")

