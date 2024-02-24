
def sumFirstN(n,sum):
    if n < 1:
        print(sum)
        return sum
    sumFirstN(n-1, sum + n)


def sumFirst(n):
    if n == 0:
        return 0
    return n + sumFirst(n-1)
    


n=5

print("\n","===============================================", "\n")
print(" Sum of First " + str(n) + " number is: \n")
sumFirstN(n, 0)
print("\n","===============================================","\n")

print(" Sum of First " + str(n) + " number is: ", sumFirst(n))
print("\n","===============================================","\n")





