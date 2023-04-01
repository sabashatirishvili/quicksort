def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        equal = []
        right = []
        for i in arr:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                right.append(i)
        return quicksort(left) + equal + quicksort(right)



arr = [9, 3, 2, 5, 6, 7,8, 23 ,13, 11, 42, 1 ,55, 3232, 22, 12]

print(quicksort(arr))