# # 16120 PPAP
# import sys
# ppap = sys.stdin.readline().strip()
# length = len(ppap)
# lst = []
# for i in range(length):
#     lst.append(ppap[i])
#
#     last = len(lst)
#     if lst[last-4:last] == ['P', 'P', 'A', 'P']:
#         for _ in range(3):
#             lst.pop()
#
# if len(lst) == 1 and lst[0] == 'P':
#     print('PPAP')
# else:
#     print('NP')

# 3190 뱀
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
# 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며.
# 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며,
# 방향 전환 정보는 X가 증가하는 순으로 주어진다.
# 6 N
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# N = int(input())
# K = int(input())
# lst = [[0 for i in range(N + 1)] for i in range(N + 1)]
# for i in range(K):
#     a, b = map(int, input().split())
#     lst[a][b] = 1
# # 뱀의 초기 위치
# queue = [(1, 1)]
# # 뱀의 이동 방향
# way = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# curway = 0
# # 반복문 종료 조건
# breaaak = False
#
# sec = 1
# L = int(input())
# LC = []
# for i in range(L):
#     x, C = input().split()
#     LC.append((int(x), C))
# LC.append((10001, 'D'))
#
# # 반복문 시작
# for X, C in LC:
#     # X초가 될 때까지 뱀은 직진한다
#     # 직진 행동을 하면: 방향대로 새로운 tuple을 추가하고, 꼬리 tuple을 삭제한다
#     while sec != X+1:
#         # 새로운 타일 / queue의 머리 + 방향
#         newX, newY = queue[-1][0] + way[curway][0], queue[-1][1] + way[curway][1]
#         print(sec, curway, "~~")
#         # newX, newY 벽부딪힘 & 중복 걸러내기..
#         # if not (0 <= newX < N) or not (0 <= newY < N) or (newX, newY) in queue:
#         if not (0 <= newX <= N):
#             breaaak = True
#             print("1T")
#             break
#         if not (0 <= newY <= N):
#             breaaak = True
#             print("2T")
#             break
#         if (newX, newY) in queue:
#             breaaak = True
#             print("3T", newX, newY)
#             break
#
#         # head
#         queue.append((newX, newY))
#         # tail
#         # 만약 사과를 먹으면 tuple을 추가하지만 꼬리 tuple은 삭제하지 않는다
#         if lst[newX][newY] == 1:
#             print(newX, newY)
#             lst[newX][newY] = 0
#         else:
#             queue.pop(0)
#         sec += 1
#         print(sec, queue)
#     # 반복문 종료 조건
#     if breaaak: break
#
#     sec = X + 1
#     # 다음 반복에 행해질 방향을 바꿔준다.
#     if C == 'D':
#         curway = (curway + 1) % 4
#     else:
#         curway -= 1
#         if curway < 0: curway + 4
# print(sec)

# # 인구 이동
# from collections import deque
#
# n, l, r = map(int, input().split())
# people_cnt = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     people_cnt.append(temp)
#
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     union = [(x, y)]
#     visited[x][y] = 1
#     while queue:
#         # print(queue)
#         x, y = queue.popleft()
#         # print(queue)
#         for i in range(4):
#             new_x = x + dx[i]
#             new_y = y + dy[i]
#             if new_x < 0 or new_y < 0 or new_x >= n or new_y >= n:
#                 continue
#             elif l <= abs(people_cnt[new_x][new_y] - people_cnt[x][y]) <= r and not visited[new_x][new_y]:
#                 union.append((new_x, new_y))
#                 queue.append((new_x, new_y))
#                 visited[new_x][new_y] = 1
#
#     if len(union) == 1:
#         return False
#     else:
#         move = 0
#         for a, b in union:
#             move += people_cnt[a][b]
#         move = move // len(union)
#
#         for a, b in union:
#             people_cnt[a][b] = move
#         return True
#         print(people_cnt)
#     return True
#
# day = 0
# # 날짜 카운트
# while True:
#     tf = False
#     visited = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j]:
#                 tf = bfs(i, j)
#                 if tf:
#                     day += 1
#     if tf == False:
#         break
#
# print(day)


# # https://www.acmicpc.net/problem/1715
# # 1715 카드 정렬하기
# # A B
# import heapq
# n = int(input())
# card = []
# for i in range(n):
#     heapq.heappush(card, int(input()))
# sum = 0
# for i in range(n):
#     if len(card)==1: break
#     tmp1 = heapq.heappop(card)
#     tmp2 = heapq.heappop(card)
#     sum += (tmp1 + tmp2)
#     heapq.heappush(card, tmp1+tmp2)
# print(sum)

# # 11404 플로이드
# # 플로이드-와샬 알고리즘
# # i, j, k 3중 for 문!
# INF = 10_000_000
#
# n = int(input()) # number of city
# m = int(input()) # number of bus
# cost = [[INF for _ in range(n)] for _ in range(n)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     cost[a-1][b-1] = min(cost[a-1][b-1], c)
# for i in range(n):
#     cost[i][i] = 0
#
# for k in range(n): # stopover city
#     for i in range(n): # departure city
#         for j in range(n): # arrival city
#             cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
#
# for i in range(n):
#     for j in range(n):
#         if cost[i][j] == INF: print(0, end=' ')
#         else: print(cost[i][j], end=' ')
#         # print(cost[i][j] if cost[i][j]!=INF else 0, end=' ')
#     print()

# # 1753 최단경로
# # graph
# INF = 10_000_000
# v, e = map(int, input().split()) # v: number of node, e: number of edge
# k = int(input()) # start node
# graph = list(v+1)
#
# for i in range(e):
#     u, v, w = map(int, input().split())
#     if graph[u][v] > w:
#         graph[u].append((v, w))
#         graph[v].append((u, w))
# for i in range(v): # itself
#     graph[i][i] = 0

# # 9663 N-Queen
# n = int(input())
# board = [0 for _ in range(n)] # [n][i]에 queen
# ans = 0
# # 해당 자리 [x][i]에 queen을 놓을 수 있는지 확인하는 함수
# def check(x):
#     for i in range(x):
#         # 해당 열에 이미 놓여져 있거나, or 대각선 조건에 걸리는 경우 False 리턴
#         if board[x]==board[i] or abs(board[x]-board[i])==abs(x-i):
#             return False
#     return True # 아무것도 걸리지 않으면 True 리턴
# # backtracking
# def bt(x):
#     global ans      # 답
#     if x == n:      # n개의 queen을 공격할 수 없게 모두 놓았음
#         ans += 1
#     else:           # 놓아야 할 queen이 남아있음
#         for i in range(n):
#             board[x] = i    # [x][i]에 queen을 놓음
#             if check(x):    # 해당 자리 [x][i]에 queen을 놓을 수 있는지
#                 bt(x+1)     # 다음 queen
#
# bt(0)
# print(ans)

# # 2580 스도쿠
# def checkLine(x, y, n): # 가로&세로 줄에 n이 있는지 확인
#     for i in range(9):
#         if n == graph[x][i] or n == graph[i][y]:
#             return False
#     return True
# def checkRect(x, y, n): # 사각형 안에 n이 있는지 확인
#     xi = x//3*3
#     yi = y//3*3
#     for i in range(3):
#         for j in range(3):
#             if n == graph[xi+i][yi+j]:
#                 return False
#     return True
# def bt(n):
#     if n == len(blank):     # 스도쿠 완성
#         for _ in range(9):
#             print(*graph[_])
#         exit()
#     for i in range(1, 10):  # 1 ~ 9까지 blank에 채워보기
#         x = blank[n][0]     # x좌표
#         y = blank[n][1]     # y좌표
#         if checkLine(x, y, i) and checkRect(x, y, i):
#             graph[x][y] = i # i를 채워놓기
#             bt(n + 1)
#             graph[x][y] = 0 # 다시 돌려놓기
#
# graph = []
# blank = []
# for i in range(9):
#     graph.append(list(map(int, input().split())))
#     for j in range(9):
#         if graph[i][j] == 0:
#             blank.append([i, j])
# bt(0)

# # 10830 행렬 제곱
# import sys
# def multi_matrix(P, Q):
#     N = len(P)
#     C = [[0 for _ in range(N)] for _ in range(N)]
#     for n in range(N):
#         for k in range(N):
#             for m in range(N):
#                 C[n][k] += (P[n][m] * Q[m][k])
#             C[n][k] %= 1000
#     return C
#
# def squ_matrix(A, B):
#     if B == 1:
#         return A
#
#     tmp = squ_matrix(A, B//2)
#
#     if B % 2 == 0:
#         return multi_matrix(tmp, tmp)
#     else:
#         return multi_matrix(multi_matrix(tmp, tmp), A)
#
# A = []
# n, B = map(int, sys.stdin.readline().strip().split())
# for i in range(n):
#     A.append(list(map(int, sys.stdin.readline().strip().split())))
#
# res = squ_matrix(A, B)
# for i in range(n):
#     for j in range(n):
#         print(res[i][j]%1000, end=' ')
#     print()
# # for i in range(n):
# #     print(' '.join(map(str, res[i])))

# # 2110 공유기 설치
# import sys
# n, c = map(int, sys.stdin.readline().strip().split())
# router = []
# for i in range(n):
#     router.append(int(sys.stdin.readline()))
# router.sort()
#
# # 이진탐색
# def binary():
#     s, e = 1, router[-1]-router[0]
#     if c == 2:
#         print(e)
#         return
#     ans = 0
#     while(s <= e):
#         mid = (s+e) // 2
#         cnt = 1
#         nearest = router[-1]-router[0]
#         before = router[0]
#         for h in router:
#             if h - before >= mid:
#                 if nearest > h-before:
#                     nearest = h-before
#                 before = h
#                 cnt += 1
#
#         if cnt >= c:
#             ans = max(ans, nearest)
#             s = mid+1
#         else:
#             e = mid-1
#     print(ans)
#
# binary()

# # 1361 두 스트링 마스크
# def samePart(s1, s2):
#     n, m = len(s1), len(s2)
#     a, b, c = 0, 0, 0
#     # 가장 긴 겹치는 부분 구하기 == LCS
#     arr = [[0 for _ in range(n)] for _ in range(m)]
#     for i in range(m):
#         for j in range(n):
#             if i == 0:
#                 if s2[i] == s1[j] and s2[i] != '*':
#                     arr[i][j] = 1
#                     if arr[i][j] > c:
#                         a, b, c = i, j, arr[i][j]
#                 else:
#                     arr[i][j] = 0
#             else:
#                 if s2[i] == s1[j] and s2[i] != '*':
#                     arr[i][j] = arr[i-1][j-1] + 1
#                     if arr[i][j] >= c:
#                         a, b, c = i, j, arr[i][j]
#                 else:
#                     arr[i][j] = 0
#     return b, a, c
#
# def mask(s1, s2):
#     # print(s1, s2)
#     if s1 == '*':
#         return s2.replace('*', '')
#     if s2 == '*':
#         return s1.replace('*', '')
#     if s1 == '' and s2 == '':
#         return ''
#     if s1 == '' or s2 == '':
#         return -1
#
#     # r은 겹치는 부분의 길이
#     # x,y는 해당부분을 가진 문자열 각각의 맨 마지막 인덱스
#     x, y, r = samePart(s1, s2)
#
#     if r != 0:  # 같은 부분이 있는 경우
#         # print("same part>> ",x, y, r)
#         start = mask(s1[:x-r+1], s2[:y-r+1])    # 1
#         mid = s1[x-r+1:x+1]                     # 2
#         end = mask(s1[x+1:], s2[y+1:])          # 3
#     else:       # 같은 부분이 없는 경우
#         try:
#             p = s1.index('*')
#             q = s2.index('*')
#         except:
#             return -1
#         # 각각 양 끝에 * 이 있으면 가능, 그렇지 않은 경우는 -1 리턴
#         # print("not same >> ", p, q)
#         if p == 0 and q == len(s2)-1:
#             start = mask(s1[0], s2[:-1])
#             mid = ''
#             end = mask(s1[1:], s2[-1:])
#         elif p == len(s1)-1 and q == 0:
#             start = mask(s1[:-1], s2[0])
#             mid = ''
#             end = mask(s1[-1], s2[1:])
#         else:
#             return -1
#
#     if start == -1 or end == -1:
#         return -1
#     else:
#         return start + mid + end
#
# s1 = input()
# s2 = input()
#
# print(mask(s1, s2))


# # 11559 Puyo Puyo
# field = []
# for i in range(12):
#     field.append(list(input()))
#
# dx = [-1,0,1,0]
# dy = [0,-1,0,1]
# visited = [[False for _ in range(6)] for _ in range(12)]
#
#
# # 같은 색의 뿌요가 모이면 터짐
# def bomb(x, y):
#     b = field[x][y]
#     field[x][y] = '.'
#     for i in range(4):
#         if 0 <= x+dx[i] < 12 and 0 <= y+dy[i] < 6 \
#                 and field[x+dx[i]][y+dy[i]] == b:
#             bomb(x+dx[i], y+dy[i])
#     return
#
# # 뿌요가 몇개 붙어 있는지 확인
# def check(x, y):
#     cha = field[x][y]
#     visited[x][y] = True
#     acc = 0
#     for i in range(4):
#         if 0 <= x+dx[i] < 12 and 0 <= y+dy[i] < 6 \
#                 and not visited[x+dx[i]][y+dy[i]] \
#                 and field[x+dx[i]][y+dy[i]] == cha:
#             acc += 1 + check(x+dx[i], y+dy[i])
#     return acc
#
#
# def puyo():
#     isbomb = 0
#     for i in range(12):
#         for j in range(6):
#             if field[i][j] != '.' and not visited[i][j]:
#                 visited[i][j] = True
#                 res = check(i, j) + 1
#                 if res > 3:
#                     isbomb = 1
#                     bomb(i, j)
#     return isbomb
#
#
# def gravity():
#     for i in range(6):
#         tmp = 11 if field[11][i] == '.' else 10
#         for j in range(10, -1, -1):
#             if field[j][i] != '.' and j != tmp:
#                 field[tmp][i] = field[j][i]
#                 field[j][i] = '.'
#             elif field[j][i] == '.':
#                 continue
#             tmp -= 1
#
#
# befo = -1
# cnt = 0
# while cnt != befo:
#     befo = cnt
#     # visited 초기화
#     visited = [[False for _ in range(6)] for _ in range(12)]
#     # 연쇄
#     cnt += puyo()
#     # print()
#     # 중력
#     gravity()
#     # for i in range(12):
#     #     print(*field[i])
#
# print(cnt)

# # 9935 문자열 폭발
# import sys
# str1 = sys.stdin.readline().strip()
# str2 = sys.stdin.readline().strip()
#
# stack = []
# elen = len(str2)
#
# for i in range(len(str1)):
#     stack.append(str1[i])
#     if ''.join(stack[-elen:]) == str2:
#         for _ in range(elen):
#             stack.pop();
#
# if stack:
#     print(''.join(stack))
# else:
#     print("FRULA")

# # 1043 거짓말
# N, M = map(int, input().split())    # N:사람의 수, M:파티의 수
# knowT = set(input().split()[1:]) # 0:진실 아는 사람 수 ~ 그 사람들의 번호
#
# parties = []
# for i in range(M):
#     parties.append(set(input().split()[1:]))
#
# for i in range(M):
#     for party in parties:
#         if party & knowT:
#             knowT = knowT.union(party)
#
# overstate = 0
# for party in parties:
#     if party & knowT:
#         continue
#     else:
#         overstate += 1
#
# print(overstate)


# # 1062 가르침
# N, K = map(int, input().split())
# words = []
# for _ in range(N):
#     words.append(input()[4:-4])
#
# base = ['a', 'c', 'i', 'n', 't']    # 기본단어
# learned = [False] * 26
# for c in base:
#     learned[ord(c)-ord('a')] = True
#
# answer = 0
#
# def back(n, cnt):
#     global answer
#     # K 개의 단어를 배웠을 떄 word를 읽을 수 있나?
#     if cnt == K:
#         tmp = 0
#         for word in words:
#             a = True
#             for c in set(word):
#                 if not learned[ord(c)-ord('a')]:
#                     a = False
#                     break
#             if a: tmp += 1 # word를 읽을 수 있음
#         answer = max(answer, tmp)
#         return
#
#     # backtracking
#     for i in range(n+1, 26):
#         if not learned[i]:
#             learned[i] = True
#             back(i, cnt+1)
#             learned[i] = False
#
#
# if K < 5:       # 5개도 못 가르칠 때, 어느 단어도 못 읽음
#     print(0)
#     exit(0)
# elif K == 26:   # 26(알파벳총개수)를 가르칠 수 있으면, 모든 단어를 읽을 수 있음
#     print(N)
#     exit(0)
#
# # 그외 : (인덱스, 지금까지 배운 알파뱃의 개수)
# back(0, 5)
# print(answer)


# # 23309 철도 공사
# ## 파이썬 시간 못.... 최적화...
# N, M = map(int, input().split())
# stations = list(input().split())
# cnstruz = []
# for _ in range(M):
#     cnstruz.append(list(input().split()))
#
# for code in cnstruz:
#     if code[0] == 'BN':   # i 다음에 설립
#         i, j = code[1], code[2]
#         if j in stations: # j가 있다면
#             continue
#
#         n = stations.index(i)
#         print(stations[(n+1)%N]) # 다음 역 출력
#         stations.insert(n+1, j)  # j 설립
#         N += 1
#
#     elif code[0] == 'BP':        # i 이전에 설립
#         i, j = code[1], code[2]
#         if j in stations:
#             continue
#
#         n = stations.index(i)
#         print(stations[n-1])    # 이전 역 출력
#         stations.insert(n, j)    # j 설립
#         N += 1
#
#     elif code[0] == 'CN': # i 다음역 폐쇄
#         i = code[1]
#         if i in stations:
#             n = stations.index(i)
#             next = stations[(n + 1) % N]
#             print(next) # 다음 역 출력
#             stations.remove(next)
#             N -= 1
#
#     elif code[0] == 'CP': # i 이전역 폐쇄
#         i = code[1]
#         if i in stations:
#             n = stations.index(i)
#             bef = stations[n-1]
#             print(bef)  # 이전 역 출력
#             stations.remove(bef)
#             N -= 1


# # 17298 오큰수
# n = int(input())
# A = list(map(int, input().split()))
#
# NGE = [-1] * n
# stack = []  # A의 인덱스 값이 저장됨
#
# for i in range(n):
#     # 스택에 A[i]을 넣다가 쌓여있는 값들보다 A[i]가 더 큰 것을 발견하면 아닐때까지 넣기
#     while stack and A[stack[-1]] < A[i]:
#         NGE[stack.pop()] = A[i]
#     stack.append(i)
#
# print(*NGE)
