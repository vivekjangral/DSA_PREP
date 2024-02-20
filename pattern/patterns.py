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

pattern11(5)