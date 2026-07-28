import heapq

n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph = [[] for _ in range(n + 1)]
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

INF = float('inf')
dist = [INF] * (n + 1)
dist[k] = 0

pq = [(0, k)]
while pq:
    d, current = heapq.heappop(pq)
    if d > dist[current]:
        continue
    for nxt, w in graph[current]:
        nd = d + w
        if nd < dist[nxt]:
            dist[nxt] = nd
            heapq.heappush(pq, (nd, nxt))

for i in range(1, n + 1):
    print(dist[i] if dist[i] != INF else -1)