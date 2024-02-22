
def isPalindrome(n):
    temp = n
    revserse = 0
    while n >0:
        lastNumber = n % 10
        n = n//10
        revserse = (revserse * 10) + lastNumber
    return temp == revserse


n=123

print("\n","===============================================", "\n")
print(" Is Number ' " + str(n) + " ' is palindrome  : ",isPalindrome(n))
print("\n","===============================================","\n")

