def frequency(arr):
    hMap={}
    for num in arr:
        if not num in hMap:
            hMap[num] = 1
        else:
            hMap[num] = hMap.get(num) + 1
    return hMap

arr = [10,5,10,15,10,5]

print("\n","===============================================", "\n")
print(" Frequency ' " + str(arr) + " ' is : ", frequency(arr))
print("\n","===============================================","\n")