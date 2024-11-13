from collections import deque

def dfs(g, s):
    Stack = deque()
    Stack.append(s)

    visited = {key: False for key in g}
    visited[s] = True

    printed_graph = list()

    while len(Stack) != 0:
        node = Stack[-1]  
        Stack.pop()       
        printed_graph.append(node)

        for neighbor in g[node]:  
            if not visited[neighbor]:
                Stack.append(neighbor)
                visited[neighbor] = True

    for i in printed_graph:
        print(i, "->", end=" ")
    print(None)

graph = {
    5: [1, 8],
    1: [5, 8, 10],
    8: [5, 1, 10],
    10: [1, 8, 20],
    20: [10, 25],
    25: [20]
}

dfs(graph, next(iter(graph)))
