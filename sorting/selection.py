def selection_sort(unsorted_arr):
    for i in range(len(unsorted_arr)):
        min_index = i
        for j in range(i+1, len(unsorted_arr)):
            if unsorted_arr[j] < unsorted_arr[min_index]:
                min_index = j
        unsorted_arr[i], unsorted_arr[min_index] = unsorted_arr[min_index], unsorted_arr[i]
    return unsorted_arr

unsorted_arr = [0,2,1,2,0]
sorted_arr = selection_sort(unsorted_arr)
print(sorted_arr)

# Time Complexity
# Worst -   O(n^2)
# Avg   -   O(n^2)
# Best  -   O(n^2)