def BFS(startNode, endNode, graph, numberNodes):
    prev = solve(startNode, graph, numberNodes)
    constructPath(startNode, endNode, prev)

def solve(startNode, graph, numberNodes):
    queue = []
    prev = [None] * numberNodes
    visited = [False] * numberNodes
    queue.append(startNode)
    visited[startNode] = True
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        for neighbor in neighbours:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                prev[neighbor] = node
    return prev

def constructPath(startNode, endNode, prev):
    path = []
    current = endNode
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()
    print(path)

graph = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]
BFS(0, 3, graph, 4)
