import random
import matplotlib.pyplot as plt

def bubble_sort_instrumented(arr):
    comparisons = 0
    swaps = 0
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1  # count each comparison
            if a[j] > a[j + 1]:
                swaps += 1  # count each swap
                a[j], a[j + 1] = a[j + 1], a[j]
    return a, comparisons, swaps

def generate_random_input(n):
    return [random.randint(0, n) for _ in range(n)]

def measure_bubble_sort(max_size, step, trials=5):
    sizes = list(range(step, max_size + 1, step))
    comp_results = []
    swap_results = []
    
    for size in sizes:
        total_comp = 0
        total_swap = 0
        for _ in range(trials):
            arr = generate_random_input(size)
            _, comp, swap = bubble_sort_instrumented(arr)
            total_comp += comp
            total_swap += swap
        comp_results.append(total_comp / trials)
        swap_results.append(total_swap / trials)
        
    return sizes, comp_results, swap_results

if __name__ == "__main__":
    max_size = 200  # Adjust maximum input size as needed
    step = 10
    sizes, comp_results, swap_results = measure_bubble_sort(max_size, step)

    # Plot the number of comparisons vs. input size
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(sizes, comp_results, 'bo-', label='Measured Comparisons')
    theoretical_comp = [size * (size - 1) / 2 for size in sizes]
    plt.plot(sizes, theoretical_comp, 'r--', label='Theoretical n(n-1)/2')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Number of Comparisons')
    plt.title('Bubble Sort Comparisons')
    plt.legend()

    # Plot the number of swaps vs. input size
    plt.subplot(1, 2, 2)
    plt.plot(sizes, swap_results, 'go-', label='Measured Swaps')
    theoretical_swaps = [size * (size - 1) / 4 for size in sizes]
    plt.plot(sizes, theoretical_swaps, 'r--', label='Theoretical n(n-1)/4')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Number of Swaps')
    plt.title('Bubble Sort Swaps')
    plt.legend()

    plt.tight_layout()
    plt.show()
