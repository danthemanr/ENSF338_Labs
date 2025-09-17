# Answers to questions are at the bottom.
import timeit

def sub_function(n):
    #the sub-function computes  the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
#the test_function calls sub-function for numbers 0 t0 9
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # the third function computes  the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

test_function()
third_function()

# 3.1. A profiler tells you various different time stats for any/all function calls that were made.
# 3.2. Benchmarking times the whole function/program/code and only gives you the overall time, but
#    profiling gives you the number of function calls, tells you how many were recursive, and
#    gives you time stats for each call of each function.
# 3.3
import cProfile
cProfile.run("test_function()\nthird_function()")
# 3.4. It seems that the function that takes the most time is third_function(), because it was
#    called only only once and took 6.465 seconds of the overall time, which was 7.081 seconds.
#    It should also be noted that, within third_function(), 100000000-1 does not equal 999.
                                                                                                