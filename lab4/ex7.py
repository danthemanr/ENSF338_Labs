import random
import timeit
import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self, elements=[]):
        self._size = len(elements)
        self.head = None
        if 0 != self.get_size():
            currNode = self.head = Node(elements[0])
            for data in elements[1:]:
                currNode.next = Node(data)
                currNode = currNode.next
    def insert_head(self, node):
        node.next = self.head
        self.head = node
        self._size = self.get_size() + 1
    def insert_tail(self, node):
        currNode = self.head
        while currNode.next != None:
            currNode = currNode.next
        currNode.next = node
        self._size = self.get_size() + 1
    def get_size(self): return self._size
    def get_element_at_pos(self, pos):
        if pos >= self.get_size():
            return None
        i = 0
        currNode = self.head
        while i < pos:
            currNode = currNode.next
            i += 1
        return currNode
    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead
    def my_reverse(self):
        prevNode = self.head
        currNode = prevNode.next
        prevNode.next = None
        while currNode.next != None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode, currNode = currNode, nextNode
        currNode.next = prevNode
        self.head = currNode

def main():
    sizes = [1000*(i+1) for i in range(4)]
    #takes a minute or two to run
    link_lists = [LinkList([random.randrange(0,size) for i in range(size)]) for size in sizes]
    avg_times1 = [timeit.timeit(lambda: link_lists[i].reverse(), number=100)/100 for i in range(len(sizes))]
    avg_times2 = [timeit.timeit(lambda: link_lists[i].my_reverse(), number=100)/100 for i in range(len(sizes))]

    a1, b1, c1 = np.polyfit(sizes, avg_times1, 2)
    a2, b2 = np.polyfit(sizes, avg_times2, 1)
    plt.figure(figsize=(10,5))
    plt.scatter(sizes, avg_times1, label=".reverse()", color="tab:orange")
    plt.plot(sizes, [a1*x*x+b1*x+c1 for x in sizes], color="tab:orange")
    plt.scatter(sizes, avg_times2, label=".my_reverse()", color="tab:blue")
    plt.plot(sizes, [a2*x+b2 for x in sizes], color="tab:blue")
    plt.title("Two Different Ways to Reverse a Linked List")
    plt.ylabel("Seconds")
    plt.xlabel("List Size")
    plt.legend()
    #plt.show()
    plt.savefig("output7.png")

if __name__ == "__main__":
    main()