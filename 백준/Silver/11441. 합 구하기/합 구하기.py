import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
psum = [0]
for i in range(N):
    psum.append(A[i]+psum[i])

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(psum[j]-psum[i-1])