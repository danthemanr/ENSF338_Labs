def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)  
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  
    left = low + 1
    right = high
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while right >= left and arr[right] > pivot:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]  # Swap misplaced elements

    arr[low], arr[right] = arr[right], arr[low]  # Swap pivot to its correct position
    return right  # Return pivot index

# Test bubble sort
arr1 = [54, 34, 43, 52, 22, 11]
bubble_sort(arr1)
print("Bubble Sorted:", arr1)

# Test quicksort
arr2 = [54, 34, 45, 12, 22, 61, 50]
quicksort(arr2, 0, len(arr2) - 1)
print("QuickSort Sorted:", arr2)




















