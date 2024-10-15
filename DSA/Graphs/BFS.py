def bfs(g,n):


    q = list()

    q.append(n)

    visited = {key: False for key in g}

    visited[n] = True

    printed_graph = list()

    while len(q) != 0:

        s = q[0]
        q.pop(0)
        printed_graph.append(s)

        for neighbor in g[s]:
            if visited[neighbor] == False:
                q.append(neighbor)
                visited[neighbor] = True


    for i in printed_graph:
        print(i, "->", end=" ")

    print(None)

graph = {
      5:  [1,8],
      1:  [5,8,10],
      8:  [5,1,10],
      10: [1,8,20],
      20: [10,25],
      25: [20]
}

bfs(graph,next(iter(graph)))