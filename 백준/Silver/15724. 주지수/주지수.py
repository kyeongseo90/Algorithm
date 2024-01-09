import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ground = []
for _ in range(N):
    ground.append(list(map(int, input().split())))

psum = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        if i==0 and j == 0:
            psum[i][j] = ground[0][0]
        elif i==0:
            psum[i][j] = psum[i][j-1]+ground[i-1][j-1]
        elif j==0:
            psum[i][j] = psum[i-1][j]+ground[i-1][j-1]
        else:
            psum[i][j] = psum[i-1][j]+psum[i][j-1]-psum[i-1][j-1]+ground[i-1][j-1]

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print(psum[x2][y2] - psum[x1-1][y2] - psum[x2][y1-1] + psum[x1-1][y1-1])