import sys
input = sys.stdin.readline
def employ():
    N = int(input())
    aplcnt = []
    for i in range(N):
        aplcnt.append(list(map(int, input().split())))
    aplcnt.sort()
    cnt = 1
    interview = aplcnt[0][1]
    for graded, gradei in aplcnt:
        if gradei < interview:
            interview = gradei
            cnt += 1
    print(cnt)

T = int(input())
for _ in range(T):
    employ()