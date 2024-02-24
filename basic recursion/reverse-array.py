def reverseArray(arr):
    if len(arr) == 0:
        return []
    return [arr[-1]] + reverseArray(arr[:-1])

def reverseArrayA(arr, left, right):
    if left >=right:
        return arr
    arr[left], arr[right-1] = arr[right-1], arr[left]
    return reverseArrayA(arr, left+1, right-1)
    



arr = [1,2,3,4,5,6]

print("\n","===============================================", "\n")
print(" Reverse of array" + str(arr) + " is: ", reverseArray(arr))
print("\n","===============================================","\n")

print("\n","===============================================", "\n")
print(" Reverse of array" + str(arr) + " is: ", reverseArrayA(arr,0,len(arr)))
print("\n","===============================================","\n")