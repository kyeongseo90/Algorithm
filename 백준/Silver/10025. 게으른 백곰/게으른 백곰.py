import sys
input = sys.stdin.readline
N, K = map(int, input().split())
locIce = []
for i in range(N):
    a, b = map(int, input().split())
    locIce.append([b,a])
locIce.sort()

l, r = 0, 0
sum = locIce[0][1]
maxsum = locIce[0][1]
while (l <= r and r < N):
    if (locIce[r][0] - locIce[l][0] <= 2*K):
        maxsum = max(maxsum, sum)

    if (locIce[r][0] - locIce[l][0] < 2*K):
        # right update
        r += 1
        if r == N:
            break
        sum += locIce[r][1]
    else: # left update
        sum -= locIce[l][1]
        l += 1

print(maxsum)