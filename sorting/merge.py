def mergeArray(arr, low, mid, high):
    array=[]
    left = low
    right = mid+1
    while left <= mid and right<=high:
        if arr[left] <= arr[right]:
            array.append(arr[left])
            left+=1
        else:
            array.append(arr[right])
            right+=1
    while left <= mid:
        array.append(arr[left])
        left+=1
    while right <= high:
        array.append(arr[right])
        right+=1
    for i in range(low, high+1):
        arr[i] = array[i-low]


def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high)//2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid+1, high)
    mergeArray(arr, low, mid, high)


arr = [2,4,3,6,7,3,4,6,1,0]
mergeSort(arr, 0, len(arr)-1)
print(arr)

# Time Complexity O(nlogn)
# space Complexity O(n)
