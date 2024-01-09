import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visit = list(map(int, input().split()))

# 누적 합 사용 > psum[i~j] = psum[i] - psum[j-1]
psum = [0]*(N+1)
# 누적 합 배열 전처리
for i in range(1, N+1):
    psum[i] = psum[i-1]+visit[i-1]

# 구하기
if psum[N-1] == 0:
    print("SAD")
else:
    maximum, cnt = 0, 0
    for i in range(X, N+1):
        tmp = psum[i]-psum[i-X]
        if maximum == tmp:
            cnt += 1
        elif maximum < tmp:
            maximum = tmp
            cnt = 1
    print(maximum)
    print(cnt)