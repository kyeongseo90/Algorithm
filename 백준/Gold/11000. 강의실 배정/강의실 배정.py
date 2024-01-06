import sys, heapq

def main():
    n = int(sys.stdin.readline())
    clss = []
    for _ in range(n):
        clss.append(list(map(int, sys.stdin.readline().split())))
    clss.sort()
    room = []
    heapq.heappush(room, clss[0][1]) # 최소힙 작은순서대로 정렬
    
    for i in range(1, n):
        if clss[i][0] < room[0]:
            heapq.heappush(room, clss[i][1]) # 새로운 강의의 끝나는 시간만 넣기
        else:
            heapq.heappop(room)
            heapq.heappush(room, clss[i][1]) # 대체된 강의의 끝나는 시간만 넣기
    print(len(room))


if __name__ == '__main__':
    main()