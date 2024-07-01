def bubble_sort(unsorted_arr):
    for i in reversed(range(len(unsorted_arr))):
        didSwap = 0
        for j in range(i-1):
            if unsorted_arr[j] > unsorted_arr[j+1]:
                temp =  unsorted_arr[j]
                unsorted_arr[j]=  unsorted_arr[j+1]
                unsorted_arr[j+1] =  temp
                didSwap = 1
        if didSwap == 0:
            break
    return unsorted_arr
                                     


# unsorted_arr = [13,54,67,32,90,7,6,4,88]
unsorted_arr = [2,3,4,5,6,7,8,9]
sorted_arr = bubble_sort(unsorted_arr)
print(sorted_arr)

# Time Complexity
# Worst -   O(n^2)
# Avg   -   O(n^2)
# Best  -   O(n)