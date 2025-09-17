import random
import timeit

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return f"Node({str(self.data)})"

class BSTree:
    def __init__(self, array=[]):
        if array == []:
            self.root = None
        else:
            self.root = Node(array[0])
            i = 1
            while i<len(array):
                self.insert(array[i])
                i += 1
    def search(self, query):
        curNode = self.root
        while curNode != None and curNode.data != query:
            if query < curNode.data:
                curNode = curNode.left
            else:
                curNode = curNode.right
        return curNode #the index would be hard to return
    def insert(self, newNode):
        if type(newNode) != Node: newNode = Node(newNode)
        if self.root == None:
            self.root = newNode
        else:
            curNode = self.root
            while True:
                if newNode.data <= curNode.data:
                    if curNode.left == None:
                        curNode.left = newNode
                        break
                    else:
                        curNode = curNode.left
                else:
                    if curNode.right == None:
                        curNode.right = newNode
                        break
                    else:
                        curNode = curNode.right

def binary_search(iterable, query, beg=0, end=None):
    if end == None: end = len(iterable)-1
    mid = (end+beg)//2
    while beg <= end:
        if iterable[mid] == query:
            return mid
        if iterable[mid] < query:
            beg = mid+1
        else:
            end = mid-1
        mid = (end+beg)//2
    return -1

def main():
    vector = [i for i in range(0, 10_000)]
    random.shuffle(vector)
    my_bst = BSTree(vector) #constructor uses the insert method
    total_time = 0
    for task in vector:
        total_time += timeit.timeit(lambda: my_bst.search(task), number=10)/10
    print(f"The total time for tree binary search was {total_time:.4e} seconds and the average time per task was {total_time/10_000:.4e} seconds.")
    vector.sort()
    total_time = 0
    for task in vector:
        total_time += timeit.timeit(lambda: binary_search(vector, task, end=9_999), number=10)/10
    print(f"The total time for array binary search was {total_time:.4e} seconds and the average time per task was {total_time/10_000:.4e} seconds.")

if __name__ == "__main__":
    main()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 4. 
#    
#    
#    
#    