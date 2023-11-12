def alternate_sort(arr):
    arr.sort()
    result = []
    while arr:
        result.append(arr.pop(0)) 
        if arr:  # check if there are still elements
            result.append(arr.pop())
    return result

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(alternate_sort(arr))
