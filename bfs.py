from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.bfs = ""
        self.found = False

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, root, search):
        visited = []
        queue = []
        self.bfs = ""
        visited.append(root)
        queue.append(root)
        while queue:
            m = queue.pop(0)
            self.bfs = self.bfs + m + " "
            if m == search:
                self.found = True
                return
            for neighbour in self.graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

g = Graph()
n = int(input("Enter the number of nodes: "))
root = input("Enter root node: ")
search = input("Enter search element: ")
print("Enter the parent-child pairs of the tree:")
for i in range(n - 1):
    parent, child = input().split()
    g.addEdge(parent, child)

g.BFS(root, search)
if g.found:
    print("Following is the Breadth-First Search:")
    print(g.bfs)
else:
    print("Given search element is not found in the tree")
