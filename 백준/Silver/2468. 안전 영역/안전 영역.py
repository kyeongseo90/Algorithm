import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

minh, maxh = sys.maxsize, 0

N = int(input())
area = []
for i in range(N):
    area.append(list(map(int, input().strip().split())))
    minh = min(minh, min(area[i]))
    maxh = max(maxh, max(area[i]))

# (i, j)를 포함한 안전지역 방문하기
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def find_safe_area(i, j, rain):
    visited[i][j] = 1
    for p in range(4):
        di = i+dx[p]
        dj = j+dy[p]
        if 0 <= di < N and 0 <= dj < N \
                and not visited[di][dj] \
                and area[di][dj] > rain:
            find_safe_area(di, dj, rain)

# 비의 양(minh~maxh)에 따른 안전지대 수 중 가장 안전지대 수가 많은 값을 찾기
result = 1
for rain in range(minh, maxh):
    visited = [[0] * N for _ in range(N)]
    num_of_safe = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > rain:
                find_safe_area(i, j, rain)
                num_of_safe += 1
    result = max(num_of_safe, result)

print(result)