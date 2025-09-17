import timeit
import random
import math
import scipy
import matplotlib.pyplot as plt

def linear_insert(iterable, query, begin, end):
    while begin <= end:
        if query >= iterable[end]:
            return end+1
        end -= 1
    return begin

def binary_insert(iterable, query, begin, end):
    mid = end//2
    while iterable[mid] != query:
        if iterable[mid] < query:
            begin = mid+1
        else:
            end = mid
        mid = (begin+end)//2
        if begin >= end: return begin
    return mid

def insertion_sort(iterable, search=linear_insert):
    end = len(iterable)
    i = 1
    while i < end:
        subject = iterable[i]
        if subject < iterable[i-1]:
            new_index = search(iterable, subject, 0, i-1)
            j = i
            while j > new_index:
                iterable[j] = iterable[j-1]
                j -= 1
            iterable[j] = subject
        i += 1
    pass

def make_vectors(lengths, max=99, sorted=False):
    vectors = []
    for length in lengths:
        vector = [random.randint(0, max) for i in range(length)]
        if sorted: vector.sort()
        vectors.append(vector)
    return vectors

def my_funct(x, quadratic, loglinear, linear, log, const):
    if type(x) != int and type(x) != float:
        return_y = [(quadratic*i*i + linear*i + loglinear*i*(math.log(i, 2)) + log*(math.log(i, 2)) + const) for i in x]
    else:
        return_y = (quadratic*x*x + linear*x + loglinear*x*(math.log(x, 2)) + log*(math.log(x, 2)) + const)
    return return_y

def main(plotnum=""):
    pts = 16
    sizes = [400*(x+1) for x in range(pts)]
    vectors = make_vectors(sizes)
    linear_times = []
    binary_times = []
    i = 0
    while  i < pts:
        vector = vectors[i]
        linear_sum = 0.0
        binary_sum = 0.0
        j = 0
        while j < 100:
            linear_sum += timeit.timeit(lambda: insertion_sort(vector), number=100)
            binary_sum += timeit.timeit(lambda: insertion_sort(vector, binary_insert), number=100)
            j += 1
        linear_times.append(linear_sum/1000/100)
        binary_times.append(binary_sum/1000/100)
        i += 1
    a1, ll1, b1, l1, c1 = scipy.optimize.curve_fit(my_funct, sizes, linear_times)[0]
    a2, ll2, b2, l2, c2 = scipy.optimize.curve_fit(my_funct, sizes, binary_times)[0]
    print(f"linear equation: ({a1})n^2 + ({ll1})nlog(n) + ({b1})n + ({l1})log(n) + {c1}")
    print(f"binary equation: ({a2})n^2 + ({ll2})nlog(n) + ({b2})n + ({l2})log(n) + {c2}")

    fig, axs = plt.subplots(1, 1, figsize=(10, 5))
    axs.scatter(sizes, linear_times)
    axs.plot(sizes, my_funct(sizes, a1, ll1, b1, l1, c1), label="linear")
    axs.scatter(sizes, binary_times)
    axs.plot(sizes, my_funct(sizes, a2, ll2, b2, l2, c2), label="binary")
    axs.set_title("making insertion sort binary")
    #axs.set_xticks(sizes)
    axs.set_xlabel("vector size")
    axs.set_ylabel("seconds")
    axs.legend()
    #plt.show()
    plt.savefig(f"output5{plotnum}.png")

if __name__ == "__main__":
    i = 1
    while False: #if True, starts slowly making plots in an infinite loop
        main(f".{i}")
        i += 1
    else:
        main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 4. They take similar time for smaller vectors but the linear version's slope increases faster,
#    causing it to diverge for bigger vectors. Insertion sort has a main loop with a nested
#    loops, where the nested loop does two things: search and insert. Insert will alwasy take
#    O(n) time, but binary search takes O(log(n)), which is faster than linear search's O(n).
#    
