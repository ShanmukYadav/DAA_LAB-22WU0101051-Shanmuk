def find_leaders(arr):
    n = len(arr)
    leaders = [arr[n - 1]]  # last element is always a leader
    max_from_right = arr[n - 1]
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)
    leaders = leaders[::-1]
    return leaders
arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr))
