# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1. line 54-58: If the new size is less than what is already
#                allocated (and greater than half the allocated
#                space), then the list is simply resized without
#                reallocation.
#    line 70:    The space to be allocated is 1.125 times the
#                new size, truncated, plus 6, rounded down to
#                the nearest multiple of 4, but not if the new
#                size is closer to this value than it is to the
#                orginal allocated space.
#    line 74-75: If that is the case, then the space to be
#                allocated is the new size rounded up to the
#                nearest multiple of 4.
#    line 77-78: If the new size is 0, then don't allocate any
#                new space.
#    line 79-90: If the space to be allocated doesn't result in
#                an array that is too big for python to handle,
#                then reallocate the array's items to a space
#                that size; if it is too big, then raise an
#                error.
#    line 91-95: point the array to the new location, change the
#                size attribute of the array, change the
#                allocated attribute of the array, and return.
#    The growth factor was implied on line 70: a number plus
#    itself bit shifted by 3 is essentially 1.125 times that
#    number.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 2.
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
import timeit
import matplotlib.pyplot as plt
if True:
    def time_append(initial_size, measures=1000):
        my_list = [1 for i in range(initial_size)]
        time_list = [0 for i in range(measures)]
        for i in range(measures):
            time_list[i] = timeit.timeit(lambda: my_list.append(1), number=1)
            my_list.pop()
        return time_list
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 3.
    time_list1 = time_append(51)
    print(f"Appending an item to a 52 item list takes about {sum(time_list1)/1000} seconds.")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 4.
    time_list2 = time_append(51)
    print(f"Appending an item to a 51 item list takes about {sum(time_list2)/1000} seconds.")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 5.
