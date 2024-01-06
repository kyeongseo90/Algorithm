T = int(input())
for _ in range(T):
    c = int(input())
    unit = [25, 10, 5, 1]
    change = [0,0,0,0]
    for i in range(4):
        change[i] = c // unit[i]
        c %= unit[i]
    print(*change)