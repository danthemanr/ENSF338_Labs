# 1. A profiler tells you various different time stats for any/all function calls that were made.
# 2. Benchmarking times the whole function/program/code and only gives you the overall time, but profiling gives you the number of function calls, tells you how many were recursive, and gives you time stats for each call of each function.
import timeit
import cProfile
import re

def sub_function(n):
    #sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)

def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

if __name__ == "__main__":
    test_function()
    third_function()