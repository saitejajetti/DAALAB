def prim(graph):
    n = len(graph)

    selected = [False] * n
    selected[0] = True

    edges = 0
    total_cost = 0

    print("Edges in MST:")

    while edges < n - 1:
        minimum = float('inf')
        x = 0
        y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            x = i
                            y = j

        print(x, "-", y, "=", minimum)

        total_cost += minimum
        selected[y] = True
        edges += 1

    print("Minimum cost:", total_cost)


graph = [
    [0, 2, 3, 0],
    [2, 0, 1, 4],
    [3, 1, 0, 5],
    [0, 4, 5, 0]
]

prim(graph)