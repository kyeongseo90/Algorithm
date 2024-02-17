import sys
import heapq
input = sys.stdin.readline


def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


while True:
    m, n = map(int, input().strip().split())
    if m + n == 0:
        break
    road = []
    allCost = 0
    for _ in range(n):
        x, y, z = map(int, input().strip().split())
        allCost += z
        heapq.heappush(road, (z, x, y))

    parent = []
    for i in range(m):
        parent.append(i) # 처음에는 자기자신을 부모로 하고있음

    # kruskal: heapq로 전력이 작은 것부터 pop해서 MST가 만들어진다면 끝
    # allCost에서 MST가 된 부분 Tree의 전력 합을 빼면 답이 됨
    sum = 0
    while road:
        cost, x, y = heapq.heappop(road)

        # 같은 tree가 아니면 union하고 내 mst에 추가하기
        if findParent(parent, x) != findParent(parent, y):
            unionParent(parent, x, y)
            sum += cost

    print(allCost - sum)