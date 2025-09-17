def merge(arr, low, mid, high):
    left = arr[low:mid+1]  
    right = arr[mid+1:high+1] 
     


    i, j, k = 0, 0, low

    # Merge two sorted subarrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy any remaining elements
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

# Helper function to print the array
def print_array(arr):
    print(" ".join(map(str, arr)))

# Testing the function
arr = [8, 42, 25, 3, 3, 2, 27, 3]
print("Original array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


