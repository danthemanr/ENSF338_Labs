# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#1. line 54-58: If the new size is less than what is already
#               allocated (and greater than half the allocated
#               space), then the list is simply resized without
#               reallocation.
#   line 70:    The space to be allocated is 1.125 times the
#               new size, truncated, plus 6, rounded down to
#               the nearest multiple of 4, but not if the new
#               size is closer to this value than it is to the
#               original allocated space.
#   line 74-75: If that is the case, then the space to be
#               allocated is the new size rounded up to the
#               nearest multiple of 4.
#   line 77-78: If the new size is 0, then don't allocate any
#               new space.
#   line 79-90: If the space to be allocated doesn't result in
#               an array that is too big for python to handle,
#               then reallocate the array's items to a space
#               that size; if it is too big, then raise an
#               error.
#   line 91-95: point the array to the new location, change the
#               size attribute of the array, change the
#               allocated attribute of the array, and return.
#   The growth factor was implied on line 70: a number plus
#   itself bit shifted by 3 is essentially 1.125 times that
#   number.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#2. The code below makes a list, repeatedly adds elements to it, and prints the capacity when it changes.
import sys
if True:
    my_list = []
    initial_size = sys.getsizeof(my_list)
    capacity = i = 0
    while i < 64:
        i += 1
        my_list.append(i)
        if capacity < (sys.getsizeof(my_list)-initial_size)/8:
            capacity = (sys.getsizeof(my_list)-initial_size)/8
            print(f"The capacity of my_list when it has {len(my_list)} elements is {capacity}.")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#3&4. The code below times appending to a list of 52 items and a list of 51 items.
import timeit
import matplotlib.pyplot as plt
def time_append(initial_size, measures=1000):
    time_list = [0 for i in range(measures)]
    for i in range(measures):
        my_list = [1 for i in range(initial_size)]
        time_list[i] = timeit.timeit(lambda: my_list.append(1), number=1)
    return time_list
if True:
    time_list1, time_list2 = time_append(52), time_append(51)
    print(f"Appending an item to a 52 item list takes about {sum(time_list1)/1000} seconds.")
    print(f"Appending an item to a 51 item list takes about {sum(time_list2)/1000} seconds.")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#5. The code below graphs the distribution of both of the timings from the last step.
    micro_secs1, micro_secs2 = [[x*1_000_000 for x in list] for list in [time_list1, time_list2]]
    b_start, b_end, b_width = 0.1, 1.0, 0.05
    b_intervals = [b_width*i+b_start for i in range(int((b_end-b_start)/b_width))]
    plt.figure(figsize=(10,5))
    plt.hist(micro_secs1, bins = b_intervals, label="52→53", color='tab:orange', alpha=0.5)
    plt.hist(micro_secs2, bins = b_intervals, label="51→52", color='tab:blue', alpha=0.5)
    plt.ylabel("Frequency")
    plt.xlabel("Microseconds")
    plt.legend()
    #plt.show()
    plt.savefig(f"output3.png")
    plt.close()
#   Yes, I do see a difference, even if the histograms do
#   overlap a fair amount. Expanding an array without having to
#   reallocate it usually takes less time but if you have to
#   reallocate, it usually takes more time. This difference is
#   because reallocation takes time.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 