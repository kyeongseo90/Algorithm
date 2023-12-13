# dp 문제. 이중for문돌면서
# j < i 인 상황에서 s[j] > s[i]일 떄 모두, max(dp[i], dp[j]+1) update 하기
n = int(input())
soldiers = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))