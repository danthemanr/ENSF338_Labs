class GraphNode:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"GraphNode({self.data})"
class Graph:
    def __init__(self):
        self.adjacency = {}  
        
    def addNode(self, data):
        node = GraphNode(data)
        if node not in self.adjacency:
            self.adjacency[node] = []
        return node

    def removeNode(self, node):
        if node in self.adjacency:
            del self.adjacency[node]
            for neighbors in self.adjacency.values():
                neighbors[:] = [pair for pair in neighbors if pair[0] != node]

    def addEdge(self, n1, n2, weight):
        if n1 in self.adjacency and n2 in self.adjacency:
            self.adjacency[n1].append((n2, weight))
            self.adjacency[n2].append((n1, weight))  

    def removeEdge(self, n1, n2):
        if n1 in self.adjacency and n2 in self.adjacency:
            self.adjacency[n1] = [pair for pair in self.adjacency[n1] if pair[0] != n2]
            self.adjacency[n2] = [pair for pair in self.adjacency[n2] if pair[0] != n1]

    def importFromFile(self, file):
        self.adjacency.clear()
        nodes = {}

        with open(file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('//'):
                    continue
                if '--' in line:
                    parts = line.replace(';', '').split('--')
                    n1_data, n2_part = parts[0].strip(), parts[1].strip()
                    if '[' in n2_part:
                        n2_data, rest = n2_part.split('[', 1)
                        weight_part = rest.split('=')[1].split(']')[0].strip()
                        weight = float(weight_part)
                    else:
                        n2_data = n2_part
                        weight = 1.0  
                    if n1_data not in nodes:
                        nodes[n1_data] = self.addNode(n1_data)
                    if n2_data not in nodes:
                        nodes[n2_data] = self.addNode(n2_data)
                    self.addEdge(nodes[n1_data], nodes[n2_data], weight)

    def __repr__(self):
        result = ""
        for node, neighbors in self.adjacency.items():
            result += f"{node.data}: {[ (n.data, w) for n, w in neighbors ]}\n"
        return result


