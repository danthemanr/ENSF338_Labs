
import time
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def get_middle(self, start, end):
        slow, fast = start, start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        return slow

    def binary_search(self, target):
        start, end = self.head, None
        while start != end:
            mid = self.get_middle(start, end)
            if mid is None:
                return False
            if mid.data == target:
                return True
            elif mid.data < target:
                start = mid.next
            else:
                end = mid
        return False

class Array:
    def __init__(self, elements):
        self.data = sorted(elements)

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

def measure_search_performance():
    sizes = [1000, 2000, 4000, 8000]
    linked_list_times = []
    array_times = []
    
    for size in sizes:
        numbers = sorted(random.sample(range(size * 10), size))
        target = numbers[size // 2]
        
        # Measure Linked List
        linked_list = LinkedList()
        for num in numbers:
            linked_list.append(num)
        
        start_time = time.time()
        linked_list.binary_search(target)
        linked_list_times.append(time.time() - start_time)
        
        # Measure Array
        array = Array(numbers)
        start_time = time.time()
        array.binary_search(target)
        array_times.append(time.time() - start_time)
    
    # Plot Results
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, linked_list_times, marker='o', label='Linked List Binary Search')
    plt.plot(sizes, array_times, marker='s', label='Array Binary Search')
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.title("Binary Search Performance: Linked List vs Array")
    plt.show()

# Run performance test
measure_search_performance()
# 1.4The complexity binary search for linked list is o(n).

