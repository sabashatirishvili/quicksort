def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
    return quicksort(left) + [pivot] +  quicksort(right)



arr = [9, 3, 2, 5, 6, 7,8, 23 ,13, 11, 42, 1 ,55, 3232, 424, 12]

print(quicksort(arr))