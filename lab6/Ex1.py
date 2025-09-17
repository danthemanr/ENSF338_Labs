import random
import timeit 

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BSTree:
    def __init__(self, array=[]):
        self.root = None
        for value in array:
            self.insert(value)

    def search(self, query):
        curNode = self.root
        while curNode is not None and curNode.data != query:
            if query < curNode.data:
                curNode = curNode.left
            else:
                curNode = curNode.right
        return curNode is not None  # Return boolean result

    def insert(self, newNode):
        if not isinstance(newNode, Node):
            newNode = Node(newNode)
        if self.root is None:
            self.root = newNode
        else:
            curNode = self.root
            while True:
                if newNode.data <= curNode.data:
                    if curNode.left is None:
                        curNode.left = newNode
                        break
                    else:
                        curNode = curNode.left
                else:
                    if curNode.right is None:
                        curNode.right = newNode
                        break
                    else:
                        curNode = curNode.right

def measure_search_time(bst, elements, trials=10):
    total_time = 0
    for elem in elements:
        time_taken = timeit.timeit(lambda: bst.search(elem), number=trials)
        total_time += time_taken
    avg_time = total_time / (len(elements) * trials)
    return avg_time, total_time

def main():
    # A sorted vector and build a BST
    sorted_vector = list(range(10000))
    bst_sorted = BSTree(sorted_vector)

    #Search performance on sorted BST
    avg_time_sorted, total_time_sorted = measure_search_time(bst_sorted, sorted_vector)
    
    #Shuffle the sorted vector and build another BST

    random.shuffle(sorted_vector)
    bst_shuffled = BSTree(sorted_vector)
    

    
    # Measure search performance on shuffled BST
    avg_time_shuffled, total_time_shuffled = measure_search_time(bst_shuffled, sorted_vector)
    # Display results
    print(f"Sorted insertion BST - Avg search time: {avg_time_sorted:.6f} sec, Total search time: {total_time_sorted:.5f} sec")
    
if __name__ == "__main__":
    main()

    # Average search is faster that total search