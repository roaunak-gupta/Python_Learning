def merge_short(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    print(f"Mid {mid}")
    left = merge_short(arr[:mid])
    right = merge_short(arr[mid:])
    print(f"{left} and {right}")
    return sorted(left + right)


li = [5,8,1,4,2,6,5,9,6,3,6,2,5,8]
result = merge_short(li)
print(result)
