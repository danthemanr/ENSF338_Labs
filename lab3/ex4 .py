import timeit
import random
import math
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
            while iterable[j] >= pivot and i<j:
                j -= 1
            if i<j:
                iterable[i], iterable[j] = iterable[j], iterable[i]
            else: break
        if iterable[j] < pivot:
            iterable[beg], iterable[j] = iterable[j], iterable[beg]
        qsort(iterable, beg, j-1)
        qsort(iterable, j+1, end)

def make_vectors(lengths, max=99, sorted=False, reversed=False):
    vectors = []
    for length in lengths:
        vector = [random.randint(0, max) for i in range(length)]
        if sorted: vector.sort()
        if reversed: vector.reverse()
        vectors.append(vector)
    return vectors

def my_funct(x, c_quadratic, c_logline):
    if type(x) != int and type(x) != float:
        return_y = []
        for i in x:
            if i == 0: return_y.append(0)
            else: return_y.append(c_quadratic*i*i + c_logline*i*(math.log(i, 2)))
    else:
        if x == 0: return_y = 0
        else:
            return_y = (c_quadratic*x*x + c_logline*x*(math.log(x, 2)))
    return return_y

def main(plotnum=""):
    interval, pts = 8000, 8 #pts must be at least 5; 8000, 8 takes ~30 mins
    sizes = [interval*(x+1) for x in range(pts)]
    vectors = make_vectors(sizes, sorted=True, reversed=True)
    times = []
    i = 0
    while  i < pts:
        vector = vectors[i]
        end = sizes[i]-1
        time_sum = 0.0
        j = 0
        while j < 10:
            print(f"{i+1}/{pts}: \t{j}/10")
            time_sum += timeit.timeit(lambda: qsort(vector, 0, end), number=50)
            j += 1
        times.append(time_sum/500)
        i += 1
    quad, log = scipy.optimize.curve_fit(my_funct, sizes, times, p0=[1.0e-10, 1.0e-7], maxfev=3200)[0]
    print(f"binary equation: ({quad})n^2 + ({log})(n)log(n)")

    fig, axs = plt.subplots(1, 1, figsize=(5, 5))
    axs.scatter(sizes, times)
    axs.plot(sizes, my_funct(sizes, quad, log))
    axs.set_xticks(sizes)
    axs.set_title("qsort")
    axs.set_xlabel("vector size")
    axs.set_ylabel("seconds")
    #plt.show()
    plt.savefig(f"./images/output4{plotnum}.png")

if __name__ == "__main__":
    i = 6
    while False:
        main(f".{i}")
        i += 1
    else:
        main()
