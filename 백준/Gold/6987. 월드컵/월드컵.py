def combination(lst, cnt):
    res = []
    def combi(c, index):
        if len(c) == cnt:
            res.append(c)
            return
        for idx, data in enumerate(lst):
            if idx > index:
                combi(c+[data], idx)
    combi([], -1)
    return res

def dfs(round):
    global result
    if round == 15:
        result = True
        for asdf in winl:
            if asdf != [0,0,0]:
                result = False
        return

    t1, t2 = game[round]
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if winl[t1][x] > 0 and winl[t2][y] > 0:
            winl[t1][x] -= 1
            winl[t2][y] -= 1
            dfs(round + 1)
            winl[t1][x] += 1
            winl[t2][y] += 1


answer = []
team = [i for i in range(6)]
game = combination(team , 2)
for i in range(4):
    result = False
    wcup = list(map(int, input().strip().split()))
    winl = [wcup[i:i+3] for i in range(0, 18, 3)]

    dfs(0)

    if result:
        print(1)
    else:
        print(0)