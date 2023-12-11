# # 10986 나머지 합
# n, m = map(int, input().split())
# lst = list(map(int, input().split()))
# for i in range(1, n): # 누적합
#     lst[i] += lst[i-1]
#
# remain = [0] * m
# remain[0] = 1
# for i in range(n):
#     remain[lst[i] % m] += 1 # 누적합을 m으로 나눈 것의 나머지를 remain[나머지값]을 증가시킴
#
# cnt = 0
# for i in remain:
#     cnt += i*(i-1)//2 # 나머지가 같은 항목 개수 중 2개를 골라 쌍을 만들 수 있음
# print(cnt)

# # 2206 벽 부수고 이동하기
# import sys
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# n, m = map(int, sys.stdin.readline().split())
#
# map = []
# for i in range(n):
#     map.append(list(sys.stdin.readline()))
#
# def bfs(x, y):
#     routeCnt = 1
#     queue = []
#     queue.append([x, y, False])
#
#     while queue:
#         cnt = len(queue)
#         routeCnt += 1
#
#         for i in range(cnt):
#
#             curX, curY, broken = queue.pop(0)
#
#             for z in range(4):
#                 tmpX, tmpY = curX+dx[z], curY+dy[z]
#                 if tmpX == n-1 and tmpY == m-1:
#                     return routeCnt
#
#                 if 0 <= tmpX < n and 0 <= tmpY < m:
#                     if map[tmpX][tmpY] == '0':  # 갈 수 있는 길이라면
#                         queue.append([tmpX, tmpY, broken])
#                         #map[tmpX][tmpY] = '1'
#                     elif broken == False:       # 갈 수 없는 길이지만, 벽을 부순 적이 없다면
#                         queue.append([tmpX, tmpY, True])
#                         #map[tmpX][tmpY] = '1'
#
#     return -1
#
# print(bfs(0,0))

# # 1865 웜홀
# import sys
# MAX = sys.maxsize
# def WARMHOLE():
#     WH = dict()
#     # 지점의 수 / 도로의 개수 / 웜홀의 개수
#     N, M, W = map(int, input().split())
#     # 도로
#     for _ in range(M):
#         a, b, c = map(int, input().split())
#         WH[a, b] = c
#         WH[b, a] = c
#         # 만약 같은 경로 있으면 최저 찾아야 하네
#     for _ in range(W):
#         a, b, c = map(int, input().split())
#         WH[a, b] = -c
#
#     # 시작노드 설정
#     s = 1
#     table = [MAX for i in range(N+1)]
#     table[s] = 0
#
#     # 모든 노드에 대해: 갈 수 있는 모든 노드 거리 계산 > 짧을 경우 갱신
#     queue = [s]
#     visited = [False for i in range(N+1)]
#
#     while queue:
#         tmp = len(queue)
#         visited[tmp] = True
#         for _ in range(tmp):
#             i = queue.pop(0)
#             for j in range(1, N+1):
#                 if not visited[j] \
#                         and (i, j) in WH \
#                         and table[i] + WH[(i, j)] < table[j]:
#                     table[j] = table[i]+WH[(i, j)]
#                     queue.append(j)
#
#     # 앞 동작을 다시 한 후, 만약 거리가 갱신된다면, -를 발생하는 음수 사이클이 존재하기에 stop
#     # YES 출력
#     s = 1
#     updated = False
#     queue.append(s)
#     visited = [False for i in range(N + 1)]
#
#     while queue:
#         tmp = len(queue)
#         visited[tmp] = True
#         for _ in range(tmp):
#             i = queue.pop(0)
#             for j in range(1, N + 1):
#                 if not visited[j] \
#                         and (i, j) in WH \
#                         and table[i] + WH[(i, j)] < table[j]:
#                     table[j] = table[i]+WH[(i, j)]
#                     queue.append(j)
#                     updated = True
#                     break
#             if updated: break
#         if updated: break
#
#     if updated:
#         print("YES")
#     else:
#         print("NO")
#
# TC = int(input())
# for _ in range(TC):
#     WARMHOLE()


# # 2482 색상환
# DIVIDED = 1000000003
# n = int(input())
# k = int(input())
#
# result = 0
# dp = [[0] * (k+1) for _ in range(n+1)]
#
# for i in range(n+1):
#     dp[i][0] = 1    # 0개를 뽑는 경우는 1가지뿐
#     dp[i][1] = i    # 1개를 뽑는 경우는 n가지
#
# for i in range(2, n+1):
#     for j in range(2, k+1):
#         if i == n:
#             dp[i][j] = dp[i-3][j-1] + dp[i-1][j]
#         else:
#             dp[i][j] = dp[i-1][j] + dp[i-2][j-1]
#         dp[i][j] %= DIVIDED
# for i in range(n+1):
#     print(*dp[i])
# print(dp[n][k])
## 이 문제는 1~N까지의 수 중 1차이가 나지 않는 K가지의 수를 뽑는 문제로 생각할 수 있음.
## 단, 1과 N은 1차이가 나는 것으로 생각.
# N/K
# 4/2 -> 1,3 / 2,4
# 5/2 -> 1,3 / 2,4 / 1,4 / 2,5 / 3,5       -> 4/2 + 1,4 / 2,5 / 3,5
# 6/2 -> 1,3 / 2,4 / 1,4 / 2,5 / 3,5 / 1,5 / 2,6 / 3,6 / 4,6
# 7/2 -> 1,3 / 2,4 / 1,4 / 2,5 / 3,5 / 1,5 / 2,6 / 3,6 / 4,6
#        / 1,6 / 2,7 / 3,7 / 4,7 / 5,7
#
# 6/3 -> 1,3,5 / 2,4,6
# 7/3 -> 1,3,5 / 2,4,6 / 1,3,6 / 1,4,6 / 2,4,7 / 2,5,7 / 3,5,7    +5
# 8/3 -> 1,3,5 / 2,4,6 / 1,3,6 / 1,4,6 / 2,4,7 / 2,5,7 / 3,5,7    +9
#        / 1,3,7 / 1,4,7 / 1,5,7 / 2,4,8 / 2,5,8 / 2,6,8 / 3,5,8 / 3,6,8 / 4,6,8


# # Combination으로 풀기 -> 시간이 너무 오래 걸림
# from itertools import *
# DIVIDED = 1000000003
# n = int(input())
# k = int(input())
#
# if k == 1:
#     print(n)
# elif k > (n / 2):
#     print(0)
# else:
#     result = 0
#     data = [i for i in range(n)]
#     combi = list(combinations(data, k))
#     for cl in combi:
#         notne = True
#         for i in range(len(cl)):
#             din = data.index(cl[i])
#             if data[din-1] in cl:
#                 notne = False
#                 continue
#         if notne: result += 1
#
#     print(result % DIVIDED)


# # 1600 말이 되고픈 원숭이
# import sys
# from collections import deque
# K = int(sys.stdin.readline())
# W, H = map(int, sys.stdin.readline().split())
# board = []
# for i in range(H):
#     board.append(list(map(int, sys.stdin.readline().split())))
#
# def outOfBoard(x, y):
#     if 0 <= x < H and 0 <= y < W: return False
#     else: return True
#
# ex, ey = H-1, W-1
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# hx = [1, 2, -2, -1, 1, 2, -1, -2]
# hy = [-2, -1, 1, 2, 2, 1, -2, -1]
# visited = [[[False] * (K+1) for _ in range(W)] for _ in range(H)]
# queue = deque()
# queue.append((0, 0, 0, 0))
# visited[0][0][0] = True
#
# while queue:
#     mx, my, mz, move = queue.popleft()
#     # 도착했어?
#     if mx == ex and my == ey:
#         print(move)
#         exit(0)
#     # 원숭이; 사방으로 가본다
#     for i in range(len(dx)):
#         x, y = mx+dx[i], my+dy[i]
#         # '보드범위 내 들어왔는지' or '벽이 있는지' or '이미 방문했는지' 확인
#         if outOfBoard(x, y) or board[x][y] or visited[x][y][mz]:
#             continue
#         else: # 원숭이; 이제 여기 가볼게
#             queue.append((x, y, mz, move+1))
#             visited[x][y][mz] = True
#     # 아직 K만큼 다 안썼다면, 말의 이동도 해보기
#     if mz < K:
#         for k in range(len(hx)):
#             p, q = mx+hx[k], my+hy[k]
#             # '보드범위 내 들어왔는지' or '벽이 있는지' or '이미 방문했는지' 확인
#             if outOfBoard(p, q) or board[p][q] or visited[p][q][mz+1]:
#                 continue
#             else: # 원숭이; 이제 여기 안가봤으면 가볼게
#                 queue.append((p, q, mz+1, move+1))
#                 visited[p][q][mz+1] = True
#
# print(-1)


# # 1111 IQ Test
# n = int(input())
# A = list(map(int, input().split()))
#
# if n == 1:
#     print("A")
#     exit(0)
# elif n == 2:
#     if A[0] == A[1]:
#         print(A[0])
#     else:
#         print("A")
#         exit(0)
#
# while


# # 1005 ACM Craft
# # 위상정렬 알고리즘 : 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열
# # 큐를 이용
# # 1. 진입차수가 0인 모든 노드를 큐에 넣는다
# # 2. 큐가 빌 때까지 다음 3,4 반복
# # 3. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
# # 4. 새롭게 진입차수가 0이 된 노드를 큐에 넣음
#
# from collections import deque
# def playACM():
#     N, K = map(int, input().split())
#     timeToBuild = deque(map(int, input().split()))  # 각 빌딩을 짓는 데 드는 시간
#     timeToBuild.appendleft(0)
#     graph = [[] for i in range(N+1)]
#     indegree = [0] * (N+1)      # 진입 차수
#
#     # 간선 정보 입력받기(선행빌딩)
#     for _ in range(K):
#         a, b = map(int, input().split())
#         graph[a].append(b)
#         indegree[b] += 1
#
#     # 승리를 위해 건설해야하는 건물 번호
#     W = int(input())
#
#     totalTime = [0] * (N+1)     # 해당 건물 완성까지 걸리는 총 시간
#     q = deque()     # 큐
#
#     # 1. 진입차수가 0인 모든 노드를 큐에 넣는다
#     # preBuild에서 0인 인덱스 큐에 추가
#     for i in range(1, N + 1):
#         if indegree[i] == 0:
#             q.append(i)
#             totalTime[i] = timeToBuild[i] # 초기 0인것은 선행 빌딩이 없기 때문에 그대로 넣어줌
#
#
#     # 2. 큐가 빌 때까지 다음 3,4 반복
#     while q:
#         # 3. 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
#         tmp = q.popleft()
#         for i in graph[tmp]:
#             indegree[i] -= 1    # 해당 노드와 연결된 빌딩들의 진입차수에서 -1
#             # 더 오래 걸리는 시간으로 업데이트
#             totalTime[i] = max(totalTime[i], totalTime[tmp]+timeToBuild[i])
#             # 4. 새롭게 진입차수가 0이 된 노드면 큐에 넣음
#             if indegree[i] == 0:
#                 q.append(i)
#
#     print(totalTime[W])
#
#
# T = int(input())
# for _ in range(T):
#     playACM()


# # 16232 아기 상어
# from collections import deque
# N = int(input())
# ocean = []
# for i in range(N):
#     ocean.append(list(map(int, input().split())))
#
# sizeOfBabyShark = 2
# cntOfEatenFish = 0
# xy = [[-1, 0], [0, -1], [0, 1], [1, 0]] #우선순위 상>좌>우>하
#
# # 가장 가까운 먹을 수 있는 물고기의 위치를 BFS로 찾기
# def findClosestFish(a, b):
#     visited = [[0] * N for _ in range(N)]
#     que = deque()
#     que.append([a, b])
#     visited[a][b] = 1
#     setOfCanEat = []
#
#     dis = 0
#     while que:
#         cntheight = len(que)
#         dis += 1
#         for _ in range(cntheight):
#             p, q = que.popleft()
#             for dx, dy in xy:
#                 x, y = p+dx, q+dy
#                 if not (0 <= x < N and 0 <= y < N):  # 못가면 빠이
#                     continue
#                 elif visited[x][y]:                  # 이미 방문했으면 빠이
#                     continue
#                 elif ocean[x][y] > sizeOfBabyShark:  # 거기에 더 큰 물고기 있어도 빠이
#                     visited[x][y] = 1                # 방문처리
#                     continue
#                 else:   # 갈 수는 있군
#                     visited[x][y] = 1                # 방문처리
#                     if ocean[x][y] != 0 and ocean[x][y] < sizeOfBabyShark:  # 만약 먹을 수 있는 물고기 있으면
#                         setOfCanEat.append([x, y, dis])
#                     else:   # 0이나 같은 크기의 물고기 -> q에 넣기
#                         que.append([x, y])
#
#     setOfCanEat.sort(key= lambda x:(x[2],x[0],x[1]))
#
#     if not len(setOfCanEat):
#         return -1, -1, -1
#     else:
#         return setOfCanEat[0]
#
# # 메인함수
# def dduruddudu():
#     global sizeOfBabyShark
#     global cntOfEatenFish
#     second = 0
#     curX, curY = 0, 0
#     for i in range(N):
#         for j in range(N):
#             if ocean[i][j] == 9:
#                 curX, curY = i, j
#     ocean[curX][curY] = 0
#
#     # 물고기 먹기 > 계속 반복
#     while True:
#         tx, ty, dis = findClosestFish(curX, curY)   # 가장 가까운 다음 먹이 위치 찾기
#         if dis == -1:           # 먹을 물고기가 없음
#             break
#         second += dis           # 시간 더해주기
#         ocean[tx][ty] = 0       # 0으로 만들어 먹어치우기
#         curX, curY = tx, ty     # 상어 위치 update
#         cntOfEatenFish += 1     # 먹었으니 먹은 개수 늘리기
#
#         # 지금까지 먹은 개수가 크기와 같으면 크기 커지기
#         if cntOfEatenFish == sizeOfBabyShark:
#             sizeOfBabyShark += 1
#             cntOfEatenFish = 0
#
#     print(second)
#
# dduruddudu()


# # 1030 프렉탈 평면
# # ex) 1 5 3 0 4 0 4
# # 시간 s=1일때 N=5개로 나눠짐 -> 가운데 K=3개X3개 정사각형이 검정색으로 칠해진다
# # ex2) 2 3 1 0 8 0 8
# # 시간 1일떄 3개로 나눠짐
# # 시간 2일때 9개로 나눠짐 가운데 1개X1개 정사각형이 검정색으로 칠해진다
# # 시간 s일때 프렉탈 평명의 크기는 N^s X N^s
#
# S, N, K, R1, R2, C1, C2 = map(int, input().split())
#
# # fractal = [[0] * (N**S) for i in range(N**S)]
# fractal = [[0 for i in range(C2-C1+1)] for j in range(R2-R1+1)]
#
# # s: 지금 시간
# # n: 한 단위 정사각형의 한변 크기
# # k: 가운데 검정색 칠해야 할 정사각형의 한변의 크기
# # s1, s2: 한 단위 정사각형의 최좌상 위치
# def recursion(s, n, k, s1, s2):
#     # 시간 끝났으면 리턴
#     if s == 0:
#         return
#     # print(s, n, k, s1, s2)
#     # # 만약 시작점이 검정색이면 작업 안해도 됨
#     # if fractal[s1][s2] == 1:
#     #     return
#
#     # 가운데 검정색 칠하기
#     tmp = (n - k) // 2
#     for i in range(s1+tmp, s1+tmp+k):
#         for j in range(s2+tmp, s2+tmp+k):
#             if R1<=i<=R2 and C1<=j<=C2:
#                 fractal[i-R1][j-C1] = 1
#
#
#     # 재귀
#     for i in range(0, N):
#         for j in range(0, N):
#             recursion(s-1, n//N, k//N, s1+n//N*i, s2+n//N*j)
#
#
# recursion(S, N**S, K*(N**(S-1)), 0, 0)
#
# for i in range(R2-R1+1):
#     for j in range(C2-C1+1):
#         print(fractal[i][j], end='')
#     print()

# # answer version
# def check_black(l, x, y):   # (x, y): 현재 탐색중인 좌표
#     center = l//N           # 검정색 칸의 범위
#
#     if l == 1:
#         return 0
#     if center * (N-K)//2 <= x < center * (N+K)//2 \
#             and center * (N-K)//2 <= y < center * (N+K)//2:
#         return 1
#     x %= center
#     y %= center
#     return check_black(l//N, x, y)
#
#
# s, N, K, R1, R2, C1, C2 = map(int, input().split())
# l = N**s    # 한 변의 길이
#
# for i in range(R1, R2+1):
#     for j in range(C1, C2+1):
#         print(check_black(l, i, j), end='')
#     print()