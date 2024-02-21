# printing pattern 
# * * * *
# * * * *
# * * * *
# * * * *

def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


# printing pattern
# *
# * *
# * * *
# * * * *
# * * * * *

def pattern2(n):
    for i in range(n):
        for j in range(i):
            print("*", end=" ")
        print("\n")

# printing pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
def pattern3(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print("\n")

# printing pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def pattern4(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i, end=" ")
        print("\n")

#printing pattern
# * * * * *
# * * * *
# * * *
# * *
# *
        
def pattern5(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print("\n")

#printing pattern
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

def pattern6(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print(j+1, end=" ")
        print("\n")

#printing pattern
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
        

def  pattern7(n):
    for i in range(n):
        for j in range(n-i-1,0, -1):
            print(" ", end=" ")
        for j in range(0,i*2+1):
            print("*", end=" ")
        for j in range(n-i-1,0, -1):
            print(" ", end=" ")
        print("\n")


# printing pattern
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
        
def  pattern8(n):
    for i in range(n, 0, -1):
        for j in range(n-i,0, -1):
            print(" ", end=" ")
        for j in range(0,i*2-1):
            print("*", end=" ")
        for j in range(n-i,0, -1):
            print(" ", end=" ")
        print("\n")

# printing pattern
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *       
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
def pattern9(n):
    pattern7(n)
    pattern8(n)

# printing pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
def  pattern10(n):
    for i in range(0, n*2):
        if i <=n:
            for j in range(i):
                print("*", end=" ")
        else:
            for j in range(n*2-i,0,-1):
                print("*", end=" ")
        print("\n")

# printing pattern
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1

def pattern11(n):
    for i in range(n):
        p=1
        if i%2 ==0:
            p=1
        else:
            p=0
        for j in range(0,i+1):
            print(p, end=" ")
            p = 1-p
        print("\n")

# printing pattern
# 1             1
# 1 2         2 1
# 1 2 3     3 2 1
# 1 2 3 4 4 3 2 1

def pattern12(n):
    s=2*(n-1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end=" ")
        for j in range(0,s):
            print(" ", end=" ")
        for j in range(i,0,-1):
            print(j, end=" ")
        print("\n")
        s = s - 2

# printing pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def pattern13(n):
    s=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(s, end=" ")
            s +=1
        print("\n")

# printing pattern
# A
# A B
# A B C
# A B C D
# A B C D E
def pattern14(n):
    for i in range(1,n+1):
        s='A'
        for j in range(1,i+1):
            print(s, end=" ")
            s = chr(ord(s)+1)
        print("\n")

# printing pattern
# A B C D E
# A B C D
# A B C
# A B
# A
def pattern15(n):
    for i in range(n):
        s='A'
        for j in range(n-i):
            print(s, end=" ")
            s = chr(ord(s)+1)
        print("\n")

# printing pattern
# A
# B B
# C C C
# D D D D
# E E E E E
def pattern16(n):
    s='A'
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(s, end=" ")
        s = chr(ord(s)+1)
        print("\n")

# printing pattern
#         A
#       A B A
#     A B C B A
#   A B C D C B A
# A B C D E D C B A
def  pattern17(n):
    for i in range(n):
        for j in range(n-i-1,0, -1):
            print(" ", end=" ")
        s ='A'
        for j in range(0,i*2+1):
            print(s, end=" ")
            if j <(i*2)//2:
                s = chr(ord(s)+1)
            else:
                s = chr(ord(s)-1)
        for j in range(n-i-1,0, -1):
            print(" ", end=" ")
        print("\n")


# printing pattern
# E
# D E
# C D E
# B C D E
# A B C D E
def pattern18(n):
    for i in range(1,n+1):
        s='A'
        s = chr(ord(s)+n-i)
        for j in range(1,i+1):
            print(s, end=" ")
            s = chr(ord(s)+1)

        print("\n")


# printing pattern
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
def pattern19(n):
    for i in range(2*n):
        if i < n:
            for j in range(n-i):
                print("*", end=" ")

            for j in range(2*i):
                print(" ", end=" ")

            for j in range(n-i):
                print("*", end=" ")
            print("\n")
        else:
            for j in range(i-n +1):
                print("*", end=" ")

            for j in range(2*(2*n-i-1)):
                print(" ", end=" ")

            for j in range(i-n+1):
                print("*", end=" ")
            print("\n")

# printing pattern
# *                 * 
# * *             * * 
# * * *         * * * 
# * * * *     * * * * 
# * * * * * * * * * * 
# * * * *     * * * * 
# * * *         * * * 
# * *             * * 
# *                 *

def pattern19(n):
    for i in range(2*n):
        if i < n:
            for j in range(i+1):
                print("*", end=" ")

            for j in range(2*n -2*i-2):
                print(" ", end=" ")

            for j in range(i+1):
                print("*", end=" ")
            print("\n")
        else:
            for j in range(2*n - i-1):
                print("*", end=" ")

            for j in range(2*i-n-3):
                print(" ", end=" ")

            for j in range(2*n - i-1):
                print("*", end=" ")
            print("\n")


# printing pattern
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
def pattern20(n):
    for i in range(n):
        for  j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print("\n")

# printing pattern
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

def  pattern21(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top =i
            left = j
            right = 2*n-2 -j
            down = 2*n-2 -i
            print(n - min(min(top, down), min(right, left)), end=" ")
        print("\n")

pattern21(4)