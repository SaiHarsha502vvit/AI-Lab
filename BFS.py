from collections import deque

def add_edge(graph, u, v):
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            traversal.append(vertex)
            visited.add(vertex)
            queue.extend(graph.get(vertex, []))

    return traversal

def main():
    graph = {}

    # Number of nodes
    n = int(input("Enter the number of nodes: "))

    # Root node
    root = int(input("Enter the root node: "))

    # Build the graph
    print("Enter the nodes connected to each node:")
    for _ in range(n):
        node = int(input(f"Enter the node: "))
        connected_nodes = list(map(int, input(f"Enter the nodes connected to node {node} separated by space: ").split()))
        for conn_node in connected_nodes:
            add_edge(graph, node, conn_node)

    # Get the target node
    target = int(input("Enter the number to check: "))

    # Check if the target node exists in the graph using BFS
    if target in bfs(graph, root):
        traversal = bfs(graph, target)
        print(f"The BFS traversal starting from node {target} is:", ' '.join(map(str, traversal)))
    else:
        print("NO")

if __name__ == "__main__":
    main()
