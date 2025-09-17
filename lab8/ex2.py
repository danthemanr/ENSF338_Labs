#from ex1 import Graph
import heapq

#the not so great option is using a linked list
class QNode:
    def __init__(self, data=None, next=None):
        if type(data) != QNode:
            self.data = data
            self.next = next
        else:
            self = data
class ListQ:
    def __init__(self, array=None):
        self.head = None
        self._size = 0
        if type(array) == list:
            for x in array:
                self.enqueue(x)
    def enqueue(self, data):
        newNode = QNode(data)
        if self.head == None:
            self.head = newNode
        else:
            curNode = self.head
            while curNode:
                if curNode.next == None:
                    curNode.next = newNode
                    break
                elif curNode.next.data > newNode.data:
                    newNode.next, curNode.next = curNode.next, newNode
                    break
                curNode = curNode.next
        self._size += 1
    def dequeue(self):
        if self.head == None:
            raise IndexError("cannot dequeue from an empty queue")
        value = self.head.data
        self.head = self.head.next
        self._size -= 1
        return value
    def peek(self):
        return self.head
    def __len__(self):
        return self._size
    def toList(self):
        array = []
        curNode = self.head
        while curNode:
            array.append(curNode.data)
            curNode = curNode.next
        return array
    def __str__(self):
        return "ListQ("+str(self.toList())+")"

class HeapQ:
    def __init__(self, array=None):
        if type(array) == list:
            self.container = heapq.heapify(array)
        else:
            self.container = []
    def enqueue(self, data):
        heapq.heappush(self.container, data)
    def dequeue(self):
        return heapq.heappop(self.container)
    def peek(self):
        return self.container[0]
    def __len__(self):
        return len(self.container)
    def __str__(self):
        return str(self.container)

