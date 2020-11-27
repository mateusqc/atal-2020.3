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


while True:
    graph = []
    [m, n] = list(map(int, input().split()))
    if m == 0 and n == 0:
        break

    for i in range(n):
        [x, y, z] = list(map(int, input().split()))
        graph.append((x, y, z))

    parent = [i for i in range(m + 1)]
    graph.sort(key=lambda node: node[2])

    print(kruskal(n))

