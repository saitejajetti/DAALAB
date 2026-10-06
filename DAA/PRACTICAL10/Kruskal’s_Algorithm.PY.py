def kruskal(vertices, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    parent = {v: v for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            parent[root_v] = root_u
            return True

        return False

    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

            if len(mst) == len(vertices) - 1:
                break

    return mst, total_cost


# Vertices
vertices = ['A', 'B', 'C', 'D']

# Edges: (source, destination, weight)
edges = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 3),
    ('C', 'D', 4),
    ('B', 'D', 5)
]

mst, cost = kruskal(vertices, edges)

print("Minimum Spanning Tree:")

for u, v, weight in mst:
    print(u, "-", v, ":", weight)

print("Total Cost:", cost)