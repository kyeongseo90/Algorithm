import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

N, M = map(int, input().split())
miro = []
for _ in range(N):
    miro.append(input().strip())

visit = [[0] * M for i in range(N)]
queue = []
queue.append((0, 0))
visit[0][0] = 1
move = 1
while queue:
    iter = len(queue)
    move += 1
    # depth를 기준으로 한 depth마다 for문을 새로 돌린다
    for i in range(iter):
        a, b = queue.pop(0)
        # (a,b)의 앞뒤양옆 길로 가본다
        for q in range(4):
            ax, by = a+dx[q], b+dy[q]
            # 구한 경우
            if ax == N-1 and by == M-1:
                print(move)
                exit(0)
            if 0 <= ax < N and 0 <= by < M \
                    and miro[ax][by] == '1' \
                    and not visit[ax][by]:
                queue.append((ax, by))
                visit[ax][by] = 1
