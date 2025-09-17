import timeit
import random
import math
import numpy as np
import scipy
import matplotlib.pyplot as plt

def linear_search(iterable, query):
    i = 0
    end = len(iterable)
    while i < end:
        if query == iterable[i]:
            return i
        i += 1
    return None

def binary_search(iterable, query, beg, end):
    subrange = mid = end//2
    while iterable[mid] != query:
        if subrange == 1:
            if iterable[end] == query:
                return end
            else:
                return None
        if iterable[mid] < query:
            beg = mid+1
        else:
            end = mid-1
        subrange = end-beg
        mid = beg + (subrange)//2
    return mid

def make_sorted_vectors(lengths, max=99):
    vectors = []
    for length in lengths:
        vector = [random.randint(0, max) for i in range(length)]
        vector.sort()
        vectors.append(vector)
    return vectors

def my_log2(x, coef, const):
    if type(x) != int and type(x) != float:
        return_y = []
        for i in x:
            return_y.append(coef * (math.log(i, 2)) + const)
    else:
        return_y = (coef * (math.log(x, 2)) + const)
    return return_y


def main(plotnum=""):
    sizes = [1000*x for x in [1, 2, 4, 8, 16, 32]]
    vectors = make_sorted_vectors(sizes)
    linear_times = []
    binary_times = []
    i = 0
    while  i < 6:
        vector = vectors[i]
        linear_sum = 0.0
        binary_sum = 0.0
        j = 0
        while j < 1000:
            end = sizes[i]-1
            look_for = vector[random.randint(0, end)]
            linear_sum += timeit.timeit(lambda: linear_search(vector, look_for), number=100)
            binary_sum += timeit.timeit(lambda: binary_search(vector, look_for, 0, end), number=100)
            j += 1
        linear_times.append(linear_sum/1000/100)
        binary_times.append(binary_sum/1000/100)
        i += 1
    print(linear_times, binary_times)
    slope, intercept = np.polyfit(sizes, linear_times, 1)
    coeficient, constant = scipy.optimize.curve_fit(my_log2, sizes, binary_times)[0]
    print(f"linear equation: {slope}(n) + {intercept}")
    print(f"binary equation: {coeficient}(log(n)) + {constant}")

    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].scatter(sizes, linear_times)
    axs[0].plot(sizes, [slope*x+intercept for x in sizes])
    axs[0].set_title("linear_search")
    axs[0].set_xlabel("vector size")
    axs[0].set_ylabel("seconds")
    axs[1].scatter(sizes, binary_times)
    axs[1].plot(sizes, [my_log2(x, coeficient, constant) for x in sizes])
    axs[1].set_title("binary_search")
    axs[1].set_xlabel("vector size")
    axs[1].set_ylabel("seconds")
    #plt.show()
    plt.savefig(f"output5{plotnum}.png")

if __name__ == "__main__":
    i = 1
    while False: #This loop will save 1 plot every 2 minutes
        main(f".{i}")
        i += 1
    else:
        main()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 4. linear_search is a linear complexity function (go figure). A linear function is of the form
#    y = mx + b, so the parameters would be x, m, and b. The timing data for linear_search was
#    able to very closely match the line with the m and b from the np.polyfit() function,
#    showing that our prediction of a linear function was very acurate.
#    The final parameters I got for y = mx + b:
#        m = 2.1634073393865073e-08
#        b = 1.8251525340469276e-06
#    
#    binary_search is a logarithmic complexity function. We predicted its log function to be of
#    the form a * log2(x) + b; I made a my_log2(x, coef, const), where coef is a and const is b.
#    I used this function in scipy.optimize.curve_fit() to get aproprite values for a and b. The
#    graphs of the binary_search times seems to be much more eratic than the linear graphs. I
#    believe that other processes on my computer were interfering with VSCode's speed at around
#    the same order of magnitude of binary_search's time; when I set the program on an infinite
#    (which is now turned off) loop for an hour AFK, the graphs it generated fit a logarithmic
#    curve much better.
#    The final parameters I got for y = (a * log2(x) + b):
#        a = 2.1602828778075634e-08
#        b = 4.370656302953894e-07
#    