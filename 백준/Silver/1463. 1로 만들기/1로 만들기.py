import sys
input = sys.stdin.readline
N = int(input())
dp = [0 for i in range(N+1)]
queue = []
queue.append((N, 0))

while queue:
    num, cnt = queue.pop(0)

    if num == 1:
        print(cnt)
        exit(0)

    if num % 3 == 0 and dp[num//3] == 0:
        queue.append((num//3, cnt+1))
        dp[num//3] = cnt+1
    if num % 2 == 0 and dp[num//2] == 0:
        queue.append((num//2, cnt+1))
        dp[num//2] = cnt+1
    if dp[num-1] == 0 and num - 1 > 0:
        queue.append((num-1, cnt+1))
        dp[num-1] = cnt+1