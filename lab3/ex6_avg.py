import timeit
import random
import math
import numpy as np
import scipy
import matplotlib.pyplot as plt

def qsort(iterable, beg, end):
    if beg < end:
        pivot = iterable[beg]
        i = beg+1
        j = end
        while i < j:
            while i<j and iterable[i] <= pivot:
                i += 1
            while iterable[j] >= pivot and j>=i:
                j -= 1
            if j>=i:
                iterable[i], iterable[j] = iterable[j], iterable[i]
            else: break
        if iterable[j] < pivot:
            iterable[beg], iterable[j] = iterable[j], iterable[beg]
        qsort(iterable, beg, j-1)
        qsort(iterable, j+1, end)

def linear_search(iterable, query):
    i = 0
    end = len(iterable)
    while i < end:
        if query == iterable[i]:
            return i
        i += 1
    return None

def binary_search(iterable, query, beg, end):
    qsort(iterable, 0, end)
    mid = (beg+end)//2
    while iterable[mid] != query:
        if iterable[mid] < query:
            beg = mid+1
        else:
            end = mid-1
        mid = (beg+end)//2
        if end <= beg+1:
            if iterable[end] == query:
                return end
            elif iterable[beg] == query:
                return beg
            else:
                return None
    return mid

def make_vectors(lengths, max=99, sorted=False):
    vectors = []
    for length in lengths:
        vector = [random.randint(0, max) for i in range(length)]
        if sorted: vector.sort()
        vectors.append(vector)
    return vectors

def my_funct(x, loglinear, linear, log, const):
    if type(x) != int and type(x) != float:
        return_y = [(linear*i + loglinear*i*(math.log(i, 2)) + log*(math.log(i, 2)) + const) for i in x]
    else:
        return_y = (linear*x + loglinear*x*(math.log(x, 2)) + log*(math.log(x, 2)) + const)
    return return_y

def main(plotnum=""):
    sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
    pts = len(sizes)
    vectors = make_vectors(sizes)
    linear_times = []
    binary_times = []
    i = 0
    #loop takes ~ 2 minutes to run
    while  i < pts:
        vector = vectors[i]
        end = sizes[i]-1
        look_for = vector[random.randint(0, end)]
        linear_sum = 0.0
        binary_sum = 0.0
        j = 0
        while j < 100:
            random.shuffle(vector)
            linear_sum += timeit.timeit(lambda: linear_search(vector, look_for), number=100)
            binary_sum += timeit.timeit(lambda: binary_search(vector, look_for, 0, end), number=100)
            j += 1
        linear_times.append(linear_sum/100)
        binary_times.append(binary_sum/100)
        i += 1
    slope, intercept = np.polyfit(sizes, linear_times, 1)
    loglin, m, log, b = scipy.optimize.curve_fit(my_funct, sizes, binary_times)[0]
    print(f"linear equation: {slope}(n) + {intercept}")
    print(f"binary equation: ({loglin})nlog(n) + ({m})n + ({log})log(n) + {b}")

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].scatter(sizes, linear_times, alpha=0.5)
    axs[0].plot(sizes, [slope*x+intercept for x in sizes])
    axs[0].set_title("linear_search")
    axs[0].set_xlabel("vector size")
    axs[0].set_ylabel("seconds for 100 random tasks")
    axs[1].scatter(sizes, binary_times, alpha=0.5)
    axs[1].plot(sizes, my_funct(sizes, loglin, m, log, b))
    axs[1].set_title("linear vs binary search")
    axs[1].set_xlabel("vector size")
    axs[1].set_ylabel("seconds for 100 random tasks")
    #plt.show()
    plt.savefig(f"./images/output6{plotnum}_avg.png")

if __name__ == "__main__":
    i = 1
    while False: #if True, starts slowly making plots in an infinite loop
        main(f".{i}")
        i += 1
    else:
        main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 4. The linear search is faster than binary search with quick sort because quick sort has
#    loglinear complexity, which is slower than the linear complexity of linear sort.
#
