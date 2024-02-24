def fibonacci(n):
    if n <=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


n=4

print("\n","===============================================", "\n")
print(" Fibonacci of  " + str(n) + " is: ", fibonacci(n))
print("\n","===============================================","\n")