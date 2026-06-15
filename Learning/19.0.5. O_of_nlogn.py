def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_short(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_short(arr[:mid])
    right = merge_short(arr[mid:])
    print(f"{left} and {right}")
    return merge(left, right)


li = [5, 8, 1, 4, 2, 6, 5, 9, 6, 3, 6, 2, 5, 8]
result = merge_short(li)
print(result)
