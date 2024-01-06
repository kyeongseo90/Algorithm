import sys
n, k = map(int, sys.stdin.readline().split())
coin = list()
for i in range(n):
    coin.append(int(sys.stdin.readline().strip()))

ans = 0
for div in reversed(coin):
    tmp, k = divmod(k, div) # 몫, 나머지
    ans += tmp

print(ans)