A, B = map(int, input().split())

def bfs(n):
    queue = [n]
    stage = 0
    stop = False
    while(queue):
        if stop: break
        stage += 1
        cnt = len(queue)
        for i in range(cnt):
            tmp = queue.pop(0)
            if tmp == B:
                stop = True
                break
            if tmp * 2 <= B:
                queue.append(tmp*2)
            if tmp*10+1 <= B:
                queue.append(tmp*10+1)

    return stage if stop else -1

print(bfs(A))