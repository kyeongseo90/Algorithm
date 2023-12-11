import sys

n, m, k = map(int, sys.stdin.readline().split())
chessboard = []
for i in range(n):
    str = list(sys.stdin.readline().rstrip())
    chessboard.append(str)

def minPaint(color):
    accsum = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            # 행+열 값이 짝수면 [0][0]과 색이 달라야함, 홀수면 [0][0]과 색이 같아야함
            if (i+j)%2 == 0:
                value = chessboard[i][j] != color
            else:
                value = chessboard[i][j] == color
            # 누적합 구하는 식
            accsum[i+1][j+1] = accsum[i][j+1]+accsum[i+1][j]-accsum[i][j]+value
    cnt = sys.maxsize
    for i in range(1, n-k+2):
        for j in range(1, m-k+2):
            # 2차원 배열 누적합 점화식, k 값
            cnt = min(cnt, accsum[i+k-1][j+k-1]-accsum[i+k-1][j-1]-accsum[i-1][j+k-1]+accsum[i-1][j-1])
    return cnt

# 두 체스판 유형 중 더 낮은 값 선택
print(min(minPaint('B'), minPaint('W')))