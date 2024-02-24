def isPalidrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return isPalidrome(string[1:-1])
    return False


n="ABCBBA"

print("\n","===============================================", "\n")
print(" Is Number ' " + str(n) + " ' is palindrome  : ", isPalidrome(n))
print("\n","===============================================","\n")