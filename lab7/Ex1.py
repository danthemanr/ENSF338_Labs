import random
import timeit
import matplotlib.pyplot as plt

# Class representing a node in the BST
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

# Binary Search Tree Implementation
class BST:
    def __init__(self):
        self.root = None

    # Insert a node into the BST iteratively 
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        if data <= parent.data:
            parent.left = Node(data, parent)
        else:
            parent.right = Node(data, parent)

    # Search for a node in the BST
    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

    # Compute the height of a given node 
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Compute the balance factor of a node
    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Retrieve balance factors for all nodes in the BST
    def get_all_balances(self, node):
        if node is None:
            return []
        return [(node.data, abs(self.balance_factor(node)))] + \
               self.get_all_balances(node.left) + \
               self.get_all_balances(node.right)


# Insert the first 1000 integers into the BST
bst = BST()
for i in range(1, 1001):
    bst.insert(i)

# Generate 1000 search tasks
search_tasks = []
numbers = list(range(1, 1001))

for _ in range(1000):
    random.shuffle(numbers)
    search_tasks.append(numbers[:])  # Store a shuffled copy

# Measure search performance & largest absolute balance
balance_values = [abs(bst.balance_factor(node)) for node, _ in bst.get_all_balances(bst.root)]
search_times = []
largest_balances = []

# Function to measure search time using timeit
def measure_search_time(task):
    """ Measures the search time of a full task using timeit """
    return timeit.timeit(lambda: [bst.search(num) for num in task], number=1)

for task in search_tasks:
    search_time = measure_search_time(task)
    search_times.append(search_time)
    largest_balances.append(max(balance_values))  # Store max balance factor in BST

# Generate Scatterplot of Balance vs. Search Time
plt.figure(figsize=(10, 6))
plt.scatter(largest_balances, search_times, alpha=0.5, color='blue')
plt.xlabel("Absolute Balance Factor")
plt.ylabel("Search Time (seconds)")
plt.title("BST Balance Factor vs. Search Time")
plt.grid(True)
plt.show()
