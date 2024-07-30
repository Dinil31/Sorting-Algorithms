def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Test the quick sort function
arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
print(arr)
sorted_arr = quick_sort(arr)
print("Sorted array is: ", end="\n")
print(sorted_arr)
