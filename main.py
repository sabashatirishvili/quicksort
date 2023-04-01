def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    # საყრდენი - პირველი, ბოლო და შუა ელემენტების მედიანი
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    pivot = sorted([first, middle, last])[1]
    
    # მასივი დავანაწილოთ ქვესიმრავლეებად რომლებიც არიან საყრდენზე ნაკლები, მეტი ან მისი ტოლი
    less = []
    equal = []
    greater = []
    for element in arr:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
    
    # საყრდენზე მეტი და ნაკლები ქვემასივების დახარისხება რეკურსიულად
    sorted_less = quicksort(less)
    sorted_greater = quicksort(greater)
    
    # დახარისხებული მასივების შეერთება და საბოლოო შედეგის მიღება
    return sorted_less + equal + sorted_greater



arr = [9, 3, 2, 5, 6, 7,8, 23 ,13, 11, 42, 1 ,55, 3232, 22, 12]

print(quicksort(arr))