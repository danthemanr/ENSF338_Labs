import timeit
import random
import matplotlib.pyplot as plt
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#3.
def linear_search(iterable, query):
    for i, x in enumerate(iterable):
        if x == query: return i
    return None

def binary_search(iterable, query, beg=0, end=None):
    if end == None: end = len(iterable)-1
    mid = (end+beg)//2
    while beg <= end:
        if iterable[mid] == query:
            return mid
        if iterable[mid] < query:
            beg = mid+1
        else:
            end = mid-1
        mid = (end+beg)//2
    return -1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#4. linear_search has O(n) worst case complexity.
#   binary_search has O(log(n)) worst case complexity.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#5.
def main():
    num_measures = 100 #measurements per task
    num_tasks = 10 #tasks per vector
    sizes = [1000*x for x in [2**(i+1) for i in range(6)]]
    vectors = [[random.randrange(0,size) for i in range(size)] for size in sizes]
    for vector in vectors: vector.sort()
    time_lists1 = [[0 for i in range(num_measures*num_tasks)] for size in sizes]
    time_lists2 = [[0 for i in range(num_measures*num_tasks)] for size in sizes]
    for i in range(len(sizes)):
        for j in range(num_tasks):
            task = random.randrange(0,sizes[i])
            for k in range(num_measures):
                time_lists1[i][j*num_measures+k] = timeit.timeit(lambda: linear_search(vectors[i], task), number=1)
                time_lists2[i][j*num_measures+k] = timeit.timeit(lambda: binary_search(vectors[i], task), number=1)
    
    b_end = 4
    b_width = 0.05
    b_intervals = [b_width*i for i in range(int((b_end)/b_width))]
    fig, axs = plt.subplots(len(sizes), 1, figsize=(6, 4*len(sizes)), constrained_layout=True)
    for i in range(len(sizes)):
        millisecs1, millisecs2 = [[x*1000 for x in arr] for arr in [time_lists1[i], time_lists2[i]]]
        axs[i].hist(millisecs1, bins=b_intervals, label="inefficient search", color='tab:orange', alpha=0.5)
        axs[i].hist(millisecs2, bins=b_intervals, label="efficient search", color='tab:blue', alpha=0.5)
        axs[i].set_title(f"Performance Distribution for size={sizes[i]}")
        axs[i].set_ylabel("Frequency")
        axs[i].set_xlabel("Milliseconds")
        axs[i].legend()
    plt.savefig(f"output4.png")

if __name__ == "__main__":
    main()