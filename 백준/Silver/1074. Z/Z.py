import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, r, c = map(int, input().split())
li = 2**N

def z(n, i, j):
    if n == 2 and i <= r < i+n and j <= c < j+n:
        if r == i and c == j:
            return 1
        elif r == i and c == j+1:
            return 2
        elif r == i+1 and c == j:
            return 3
        else:
            return 4

    res = 0
    if r < i+n//2 and c < j+n//2:
        res += z(n//2, i, j)
    elif r < i+n//2 and c < j+n:
        res += (n//2) ** 2
        res += z(n//2, i, j+n//2)
    elif r < i+n and c < j+n//2:
        res += ((n//2) ** 2) * 2
        res += z(n//2, i+n//2, j)
    elif r < i+n and c < j+n:
        res += ((n//2) ** 2) * 3
        res += z(n//2, i+n//2, j+n//2)

    return res


print(z(2**N, 0, 0)-1)