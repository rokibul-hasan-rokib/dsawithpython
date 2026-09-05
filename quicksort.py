def quickShort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]
    left = []
    right = []
    
    for x in arr[:-1]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    
    return quickShort(left) + [pivot] + quickShort(right)


print(quickShort([1, 5, 2, 6, 3, 7, 4]))