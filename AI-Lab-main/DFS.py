def add_edge(graph, u, v):
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]


# Hello ramantey vacheysindha cheyli ni paina e prema  



def dfs(graph, node, visited, traversal=[]):
    visited[node] = True
    traversal.append(node)
    for neighbour in graph.get(node, []):
        if neighbour not in visited:



            dfs(graph, neighbour, visited, traversal)
    return traversal

def main():
    graph = {}
    visited = {}

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




# Hello ramantey vacheysindha cheyli ni paina e prema 



    # Get the target node
    target = int(input("Enter the number to check: "))

    # Perform DFS to check if target exists in the graph
    if dfs(graph, root, {}) and target in graph:
        traversal = dfs(graph, target, {})
        print(f"The DFS traversal starting from node {target} is:", ' '.join(map(str, traversal)))
    else:
        print("NO")

if __name__ == "__main__":
    main()




# Hello ramantey vacheysindha cheyli ni paina e prema 