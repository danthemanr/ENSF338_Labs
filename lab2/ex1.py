# Question 1,2,3 and 5 with their answers as comments:
#1.What does this code do?
#The function recursively computes the Fibonacci number at position n.
#2.Is this an example of a divide-and-conquer algorithm (think carefully about this one)? 
#NO
#3.Give an expression for the time complexity of the algorithm.
#O(n^2)
#5.Give an expression for the time complexity of the optimized algorithm.
#O(n)
#
#4.code
def func_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = func_memo(n-1, memo) + func_memo(n-2, memo)
    return memo[n]


#6.code
import timeit
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

# Memoized Fibonacci function
def func_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = func_memo(n-1, memo) + func_memo(n-2, memo)
    return memo[n]

# Timing setup
n_values = list(range(36))
times_recursive = []
times_memoized = []

for n in n_values:
    # Measure time for recursive function
    recursive_time = timeit.timeit(lambda: func(n), number=1)  # Run once to simulate real execution time
    times_recursive.append(recursive_time)

    # Measure time for memoized function
    memoized_time = timeit.timeit(lambda: func_memo(n), number=1)
    times_memoized.append(memoized_time)


plt.figure(figsize=(8, 6))
plt.plot(n_values, times_recursive, marker='o', label="Recursive Fibonacci (O(2ⁿ))")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Execution Time of Recursive Fibonacci Function (timeit)")
plt.legend()
plt.grid()
plt.savefig("ex1.6.1.jpg")
plt.show()

# Plot results for memoized function
plt.figure(figsize=(8, 6))
plt.plot(n_values, times_memoized, marker='o', color='r', label="Memoized Fibonacci (O(n))")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Execution Time of Memoized Fibonacci Function (timeit)")
plt.legend()
plt.grid()
plt.savefig("ex1.6.2.jpg")
plt.show()


