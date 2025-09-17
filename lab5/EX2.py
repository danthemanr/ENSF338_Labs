import timeit

class PriorityQueueMergeSort:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
        self.queue = self.mergesort(self.queue)  # Sorting after each insertion
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

class PriorityQueueSortedInsert:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        if self.is_empty():
            self.queue.append(value)
        else:
            for i in range(len(self.queue)):
                if self.queue[i] > value:
                    self.queue.insert(i, value)
                    return
            self.queue.append(value)  
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
  # measure the performance 
  
