A = []
n, m = map(int, input().split())
for i in range(n):
    A.append(list(map(int, input().split())))
B = []
m, k = map(int, input().split())
for i in range(m):
    B.append(list(map(int, input().split())))
C = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for p in range(m):
            C[i][j] += A[i][p] * B[p][j]

for i in C:
    print(' '.join(map(str,i)))