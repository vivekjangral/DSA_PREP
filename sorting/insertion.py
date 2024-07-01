def insertion_sort(unsorted_arr):
    for i in range(len(unsorted_arr)):
        j=i
        while j>0 and unsorted_arr[j-1] > unsorted_arr[j]:
            temp = unsorted_arr[j-1]
            unsorted_arr[j-1] = unsorted_arr[j]
            unsorted_arr[j] = temp
            j -=1
    return unsorted_arr
                                     


# unsorted_arr = [13,54,67,32,90,7,6,4,88]
unsorted_arr = [1,2,3,4,5,6,7,8,9]
sorted_arr = insertion_sort(unsorted_arr)
print(sorted_arr)

# Time Complexity
# Worst -   O(n^2)
# Avg   -   O(n^2)
# Best  -   O(n)