import sys
input = sys.stdin.readline

N = int(input())
map = []
for _ in range(N):
    map.append(input().strip())

visit = [[0] * N for _ in range(N)]
group = []

def bfs_find_village(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = []
    queue.append((x, y))
    visit[x][y] = 1
    house = 1
    while queue:
        a, b = queue.pop()
        # (a, b)의 앞뒤양옆에 집이 있으면 queue에 추가
        for i in range(4):
            ax, by = a+dx[i], b+dy[i]
            if 0 <= ax < N and 0 <= by < N \
                    and visit[ax][by] == 0 \
                    and map[ax][by] == '1':
                queue.append((ax, by))
                # (ax, by) 방문 처리, 집 수 +1
                visit[ax][by] = 1
                house += 1
    return house

for i in range(N):
    for j in range(N):
        # 이전에 방문하지 않은 집들만 방문한다
        if map[i][j] == '1' and not visit[i][j]:
            # 단지 내 집 개수를 추가한다
            # (i, j)와 인접한 집들을 찾아 visited 처리한다.
            group.append(bfs_find_village(i, j))

print(len(group))
group.sort()
for i in group:
    print(i)