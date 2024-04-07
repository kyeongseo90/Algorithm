def combination(arr, cnt):
    result = []

    def combi(add, idx):
        if len(add) == cnt:
            result.append(add)
            return
        for id, data in enumerate(arr):
            if id > idx:
                combi(add + [data], id)

    combi([], -1)
    return result

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

def power(member):
    full = 0
    for i in member:
        for j in member:
            if i != j:
                full += S[i-1][j-1]
    return full

result = 10e9
for members in combination(list(i for i in range(1, N+1)), N//2):
    # 뽑힌 멤버들의 능력치 구하기
    power1 = power(members)

    # 뽑히지 못한 멤버들의 능력치 구하기
    members2 = list(i for i in range(1, N + 1))
    for i in members:
        members2.remove(i)
    power2 = power(members2)
    # 차를 구해서 최소값이면 update
    result = min(result, abs(power2-power1))

print(result)