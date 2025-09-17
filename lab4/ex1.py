import time
import matplotlib.pyplot as plt
import numpy as np

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = ListNode(value)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ListNode(value)
    
    def binary_search(self, target):
       
        values = []
        temp = self.head
        while temp:
            values.append(temp.value)
            temp = temp.next
        
        #  binary search on the array
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid] == target:
                return True
            elif values[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

class Array:
    def __init__(self, data):
        self.data = sorted(data)  
        # sorted data for binary search

    def binary_search(self, target):
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data[mid] == target:
                return True
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

def compare_search_times():
    sizes = [1000, 2000, 4000, 8000]
    linked_list_durations = []
    array_durations = []

    for size in sizes:
        dataset = list(range(size))  # Sorted data

        #  linked list
        linked_list = LinkedList()
        for item in dataset:
            linked_list.append(item)
        
        #  array
        array_wrapper = Array(dataset)
        
        # Time linked list search
        start = time.time()
        linked_list.binary_search(size // 2)
        linked_list_durations.append(time.time() - start)
        
        # Time array search
        start = time.time()
        array_wrapper.binary_search(size // 2)
        array_durations.append(time.time() - start)
    
    # Plot performance comparison
    plt.plot(sizes, linked_list_durations, marker='o', label='Linked List')
    plt.plot(sizes, array_durations, marker='s', label='Array')
    plt.xlabel('Data Size')
    plt.ylabel('Time (seconds)')
    plt.title('Performance of Binary Search in Linked List vs Array')
    plt.legend()
    plt.show()


"""
Ex1.4 Binary search in an array is O(log n) because elements are directly accessible by index.
For a linked list, finding the middle element requires O(n), making the overall complexity O(n).
This makes binary search in a linked list significantly slower than in an array.
"""

if __name__ == "__main__":
    compare_search_times()