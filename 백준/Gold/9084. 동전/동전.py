import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1) # i원을 만들 수 있는 경우의 수
    dp[0] = 1
    # 각 동전마다 만들 수 있는 경우를 찾는다
    for c in coin:
        for i in range(0, M+1):
            # i번째 돈을 만드는 경우는 dp[i-동전단위]와 같다.
            if i >= c:
                dp[i] += dp[i-c]
    print(dp[M])