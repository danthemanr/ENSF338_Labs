import timeit
import random
import json
import matplotlib.pyplot as plt

# 1. (algorithm code)
def binary_search(iterable, query, beg, end, mid=None):
    if mid == None: mid = (beg+end)//2
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

def interpolate_iterable(iterable, y, beg, end):
    if iterable[end] == iterable[beg]: #avoids division by zero
        x = (end+beg)//2
    else:
        x = int((y-iterable[beg])*(end-beg)/(iterable[end]-iterable[beg])+beg)
    return x

def main(plotnum=""):
    with open("lab_data/ex7data.json", 'r') as in_file:
        array = json.load(in_file)
    with open("lab_data/ex7tasks.json", 'r') as in_file:
        tasks = json.load(in_file)

# 2. (measurement code)
    end = len(array)-1
    x1_values = [tasks[int(i//10)] for i in range(10*len(tasks))]
    y1_values = []
    y2_values = []
    for i in range(len(tasks)):
        for j in range(10):
            midpoint = random.randint(0, end)
            y1_values.append(timeit.timeit(lambda: binary_search(array, tasks[i], 0, end, midpoint), number=100)/100)
        midpoint = interpolate_iterable(array, tasks[i], 0, end)
        y2_values.append(timeit.timeit(lambda: binary_search(array, tasks[i], 0, end, midpoint), number=100)/100)

# 3. (plotting code)
    fig, axs = plt.subplots(1, 1, figsize=(15, 5))
    axs.scatter(x1_values, y1_values, alpha=0.5, label="random midpoint")
    axs.scatter(tasks, y2_values, alpha=0.5, label="linear interpolation midpoint")
    axs.set_title("performance of linear interpolation or random midpoint searching")
    axs.set_xlabel("task (check if this number in array)")
    axs.set_ylabel("time taken")
    axs.legend()
    #plt.show()
    plt.savefig(f"output7{plotnum}.png")

if __name__ == "__main__":
    i = 1
    while False: #if True, starts making plots in an infinite loop
        main(f".{i}")
        i += 1
    else:
        main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 4. If you include the processing time for calculating the midpoint, then interpolation sort
#    seems to actually be slower for this size of list. If you remove this time (like I have in
#    the code), then the interpolation seems about the same (but maybe a bit faster). What makes
#    interpolation sort better is that the time it takes doesn't grow as fast relative to the
#    list as plain binary search.
#
