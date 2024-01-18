import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))

good = 0
a.sort()
for i in range(N):
    st, end = 0, N-1
    while (st < end):
        if a[st] + a[end] == a[i]:
            if i != st and i != end:
                good += 1
                break
            elif i == st:
                st += 1
            elif i == end:
                end -= 1
        elif a[st] + a[end] > a[i]:
            end -= 1
        else:
            st += 1
print(good)