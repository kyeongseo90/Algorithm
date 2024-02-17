import sys
input = sys.stdin.readline

def dfs(origin, ride):
    for dest in airplane[origin]:
        if not visited[dest]:
            visited[dest] = True
            ride = dfs(dest, ride+1)
    return ride

T = int(input())
for _ in range(T):
    N, M = map(int, input().strip().split())
    airplane = [[] for i in range(N+1)]
    visited = [False] * (N+1)
    for i in range(M):
        a, b = map(int, input().strip().split())
        airplane[a].append(b)
        airplane[b].append(a)
    # 방문하지 않은 국가(0)라면 방문해야함
    # 이미 방문한 국가라면 비행기 종류를 늘리지 않아도 됨
    # dfs로 가보지 않은 국가만 간다
    visited[1] = True
    print(dfs(1, 0))