class GraphNode:
    def __init__(self, data=None, adj=None):
        if type(data) != GraphNode:
            self.data = data
            self.adj = adj
        else:
            self = data
class Edge:
    def __init__(self, ref, next=None, weight=None):
        self.ref = ref
        self.next = next
        if weight:
            self.weight = weight
        else:
            self.weight = 1
        

class Graph:
    def __init__(self, file=None, _weighted=True, _directed=False, _multi=False):
        self.container = []
        self._weighted = _weighted
        self._directed = _directed
        self._multi = _multi
        if file:
            self.importFromFile(file)
    def addNode(self, data):
        newNode = GraphNode(data)
        if newNode not in self.container:
            self.container.append(newNode)
        return newNode
    def removeNode(self, oldNode):
        self.container.remove(oldNode)
        for vertex in self.container:
            self._disconnect(vertex, oldNode)
    def addEdge(self, n1, n2, weight=None):
        if weight:
            if weight != 1:
                raise ValueError("tried to weight an edge in a non-weighted graph")
            w = weight
        else:
            w = 1
        if self._disconnect(n1, n2) and not self._multi:
            print("Warning: tried to insert multiple edges into a graph that isn't a multigraph; operation undone.")
        n1.adj = Edge(n2, next=n1.adj.next, weight=w)
        if not self._directed:
            if self._disconnect(n2, n1) and not self._multi:
                print("Warning: tried to insert multiple edges into a graph that isn't a multigraph; operation undone.")
            n2.adj = Edge(n1, next=n2.adj.next, weight=w)
    def removeEdge(self, n1, n2):
        self._disconnect(n1, n2)
        if not self.directed:
            self._disconnect(n2, n1)
    def _disconnect(self, n1, n2):
        curNode = n1.adj
        if curNode != None and curNode.ref == n2:
            n1.adj = curNode.next
        while curNode.next != None:
            if curNode.next.ref == n2:
                curNode.next = curNode.next.next
                return True
            curNode = curNode.next
        return False
    def importFromFile(self, file):
        self.container = []
        ...
