import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    x = list(map(int, input().strip().split()))

    maxSubSum = -10e9
    for i in range(N):
        subSub = x[i]
        maxSubSum = max(maxSubSum, subSub)
        for j in range(i+1, N):
            subSub += x[j]
            maxSubSum = max(maxSubSum, subSub)
    print(maxSubSum)