def factorial(n):
    if n == 0:
        return 1
    return n* factorial(n-1)


n=3

print("\n","===============================================", "\n")
print(" Factorial of  " + str(n) + " is: ", factorial(n))
print("\n","===============================================","\n")