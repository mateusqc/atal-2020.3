graph = []
parent = []
cost = 0

def find(a):
    global parent
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def merge(x, y, k):
    global parent
    global cost
    global graph
    i = find(x)
    j = find(y)
    if i != j:
        cost -= graph[k][2]
        if i > j:
            parent[i] = j
        else:
            parent[j] = i


while True:
    graph = []
    cost = 0
    try:
        [m, n] = list(map(int, input().split()))
    except EOFError:
        break

    if m == 0 and n == 0:
        break

    parent = [i for i in range(n + 1)]

    for i in range(n):
        [x, y, z] = list(map(int, input().split()))
        graph.append((x, y, z))
        cost += z
    
    graph.sort(key=lambda node: node[2])
    for i in range(n):
        merge(graph[i][0], graph[i][1], i)

    print(cost)



