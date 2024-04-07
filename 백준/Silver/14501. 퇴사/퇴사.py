N = int(input())
T = []
P = []
for i in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

# dp[i] i날까지 얻을 수 있는 최대 이익
dp = [0 for i in range(N+1)]

for i in range(N-1, -1, -1):
    if i + T[i] <= N: #인 경우에만 상담을 할 수 있음
        # i날에 상담을 안하는 것과, 상담을 하는 것 중 큰 것 선택
        dp[i] = max(dp[i+1], P[i] + dp[i + T[i]])
    else:
        dp[i] = dp[i+1]
print(max(dp))