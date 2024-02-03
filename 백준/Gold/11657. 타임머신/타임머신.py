import sys
inf = sys.maxsize
input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
dist = [inf]*(N+1)
dist[1] = 0

# N 번 반복
for i in range(N):
    # 모든 간선 확인
    for cur, next, cost in edges:
        if dist[cur] != inf and dist[cur] + cost < dist[next]:
            dist[next] = dist[cur]+cost
            # 만약 N-1 번째에 갱신이 있다면 음의 사이클이 있다는 것.
            if i == N-1:
                print(-1)
                exit(0)

for i in range(2, N+1):
    if dist[i] == inf:
        print(-1)
    else:
        print(dist[i])