graph = []
parent = []

def kruskal(c):
    global parent
    global graph
    ans = 0
    for i in range(c):
        u = find(graph[i][0])
        v = find(graph[i][1])
        if v != u:
            parent[u] = parent[v]
            ans += graph[i][2]
    return ans

def find(a):
    global parent
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

[n, m] = list(map(int, input().split()))

for i in range(m):
    [u, v, c] = list(map(int, input().split()))
    graph.append((u, v, c))

parent = [i for i in range(n + 1)]
graph.sort(key=lambda node: node[2])

print(kruskal(m))

