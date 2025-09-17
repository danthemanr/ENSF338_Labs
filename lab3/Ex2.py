import time
import random
import numpy as np
import matplotlib.pyplot as plt

def bubble_sort(arr):
    a = arr.copy()  
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                # Swap using a temporary variable
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return a


# Quicksort 

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while right >= left and arr[right] >= pivot:
            right = right - 1
        if right < left:
            done = True
        else:
            # Swap elements at left and right indices
            arr[left], arr[right] = arr[right], arr[left]
    # Place the pivot in its correct position
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        # Recursively sort elements before and after partition
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def quicksort_wrapper(arr):
    a = arr.copy()
    if a:  # Check for non-empty list
        quicksort(a, 0, len(a) - 1)
    return a


# Timing Function
def time_function(sort_func, arr, repeats=3, use_wrapper=False):
    start = time.perf_counter()
    for _ in range(repeats):
        if use_wrapper:
            sort_func(arr)
        else:
            sort_func(arr)
    end = time.perf_counter()
    return (end - start) / repeats

# Test Case Generator
def generate_cases(n):
    # Best-case: already sorted list (for bubble sort, nearly O(n))
    best = list(range(n))
    # Worst-case: reverse sorted list (for bubble sort, worst-case quadratic)
    worst = list(range(n, 0, -1))
    # Average-case: a random list
    average = [random.randint(0, n) for _ in range(n)]
    return best, worst, average


# Main Testing & Plotting
def main():
    # Define 20 different input sizes 
    sizes = np.linspace(10, 1000, 20, dtype=int)
    
    # Dictionaries to store timing results for bubble sort and quicksort.
    times_bubble = {'best': [], 'worst': [], 'average': []}
    times_quick  = {'best': [], 'worst': [], 'average': []}
    
    for n in sizes:
        best_case, worst_case, average_case = generate_cases(n)
        
        # Time bubble sort on best, worst, and average cases.
        t_bubble_best  = time_function(bubble_sort, best_case)
        t_bubble_worst = time_function(bubble_sort, worst_case)
        t_bubble_avg   = time_function(bubble_sort, average_case)
        
        times_bubble['best'].append(t_bubble_best)
        times_bubble['worst'].append(t_bubble_worst)
        times_bubble['average'].append(t_bubble_avg)
        
        # For quicksort
   
        t_quick_worst = time_function(quicksort_wrapper, best_case, use_wrapper=True)
        t_quick_best  = time_function(quicksort_wrapper, average_case, use_wrapper=True)
        t_quick_avg   = t_quick_best  # In this implementation, best and average are similar.
        
        times_quick['best'].append(t_quick_best)
        times_quick['worst'].append(t_quick_worst)
        times_quick['average'].append(t_quick_avg)
    
    # Generate plots for each scenario.
    scenarios = ['best', 'worst', 'average']
    for scenario in scenarios:
        plt.figure(figsize=(8, 5))
        plt.plot(sizes, times_bubble[scenario], label='Bubble Sort', marker='o')
        plt.plot(sizes, times_quick[scenario], label='Quicksort', marker='s')
        plt.xlabel('Input Size (n)')
        plt.ylabel('Time (seconds)')
        plt.title(f'Performance Comparison ({scenario.capitalize()} Case)')
        plt.legend()
        
        # For the average-case plot, highlight the first input size where quicksort beats bubble sort.
        if scenario == 'average':
            for i, (tb, tq) in enumerate(zip(times_bubble[scenario], times_quick[scenario])):
                if tq < tb:
                    plt.scatter(sizes[i], tq, color='red', s=80, zorder=5)
                    plt.annotate(f'n={sizes[i]}', (sizes[i], tq),
                                 textcoords="offset points", xytext=(0,10), ha='center')
                    break
        
        plt.tight_layout()
        plt.savefig(f'performance_{scenario}.png')
        # Uncomment the next line to display the plots interactively.
        # plt.show()
    
    # Determine the threshold (from average-case timings) where quicksort becomes faster.
    threshold = None
    for i, (tb, tq) in enumerate(zip(times_bubble['average'], times_quick['average'])):
        if tq < tb:
            threshold = sizes[i]
            break
    print("Suggested threshold input size (average case):", threshold)

if __name__ == '__main__':
    main()