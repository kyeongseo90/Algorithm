import sys
from queue import PriorityQueue
inf = sys.maxsize
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
graph = [[] * (V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    # if graph[u][v] > w:
    #     graph[u][v] = w

dijstra = [inf] * (V+1)
dijstra[K] = 0

que = PriorityQueue()
que.put((0, K))
while not que.empty():
    weight, node = que.get()
    # 갱신
    if dijstra[node] < weight:
        continue
    # node와 연결된 다른 노드들을 큐에 삽입
    # for i in range(V):
    for next, edge in graph[node]:
        next_weight = weight + edge
        if dijstra[next] > next_weight:
            dijstra[next] = next_weight
            que.put((next_weight, next))

for i in range(1, V+1):
    if dijstra[i] == inf:
        print("INF")
    else:
        print(dijstra[i])