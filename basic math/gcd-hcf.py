from math import sqrt

def gcd(n1,n2):
    gcd =0
    for i in range(1,min(n1,n2)+1):
        if n1%i ==0 and n2 % i == 0:
            gcd = i
    return gcd

def gcd_A(n1,n2):
    for i in range(min(n1,n2)+1, 0 ,-1):
        if n1%i ==0 and n2 % i == 0:
            return i
    return 0

# Euclidean Algorithm
def gcd_B(n1,n2):
    while  n1 >0 and n2 >0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    if n1 == 0:
        return n2
    else:
        return n1


    


n1=20
n2 = 40

print("\n","===============================================", "\n")
print(" GCD of gcd(" + str(n1) + ',' + str(n2) + ") is : ",gcd(n1, n2))
print("\n","===============================================","\n")

print("\n","===============================================", "\n")
print(" GCD of gcd(" + str(n1) + ',' + str(n2) + ") is : ",gcd_A(n1, n2))
print("\n","===============================================","\n")

print("\n","===============================================", "\n")
print(" GCD of gcd(" + str(n1) + ',' + str(n2) + ") is : ",gcd_B(n1, n2))
print("\n","===============================================","\n")

