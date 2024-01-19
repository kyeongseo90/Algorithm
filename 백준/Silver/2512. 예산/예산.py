import sys
input = sys.stdin.readline

N = int(input())
city = list(map(int, input().split()))
total_budget = int(input())

start, end = 0, max(city)
mid = (start + end) // 2

while start <= end:
    # 상한가가 mid일 때 사용될 예산 총 값 구하기
    use_budget = 0
    for i in range(N):
        if mid < city[i]:
            use_budget += mid
        else:
            use_budget += city[i]
    # binary search
    if use_budget == total_budget:
        break
    elif use_budget > total_budget:
        end = mid - 1
        mid = (start + end) // 2
    else:
        start = mid + 1
        mid = (start + end) // 2

print(mid)