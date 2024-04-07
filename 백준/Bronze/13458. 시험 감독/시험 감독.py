import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = N
for i in range(N):
    result += max(math.ceil((A[i]-B) / C), 0)
print(result)