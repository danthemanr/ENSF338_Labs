# Ex4.1 Array
class ArrayQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.insert(0, value)  #element insertion at head 

    def dequeue(self):  #removing an element from the tail
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.queue.pop()  

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):#Getting the last element 
        if self.is_empty():
            return None
        return self.queue[-1]  

    def size(self):
        return len(self.queue)
    
    def __str__(self):
        return " <- ".join(map(str, self.queue))

#4.2 using single linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None  
        self.tail = None  
    
    def enqueue(self, value):#head insertion
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node  
    
    def dequeue(self):#taiol delete
        if not self.head:
            raise IndexError("Dequeue from empty queue")

        if self.head == self.tail:  
            value = self.head.value
            self.head = self.tail = None
            return value

        # Traverse to find the node before the tail
        current = self.head
        while current.next != self.tail:
            current = current.next

        value = self.tail.value
        self.tail = current
        self.tail.next = None  
        return value

    def is_empty(self):
        return self.head is None

    def peek(self):
        """Return the tail element without removing it."""
        return self.tail.value if self.tail else None

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " <- ".join(values)
