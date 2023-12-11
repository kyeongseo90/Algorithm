# # 12851 숨바꼭질 2
# import sys
# MAX = 100000
# n, k = map(int, sys.stdin.readline().split())
# q = [n]
# #    [[depth, count]]
# visit = [[-1, 0] for _ in range(MAX+1)]
# visit[n][0] = 0
# visit[n][1] = 1
# turn = [False, 0]
#
# while len(q) != 0:
#     front = q.pop(0)
#     if front == k:
#         turn[0] = True
#         turn[1] = len(q)
#     for nxt in [front-1, front+1, front*2]:
#         if 0 <= nxt <= MAX:
#             # 처음뵙는숫자입니당 queue에 넣어요
#             if visit[nxt][0] == -1:
#                 q.append(nxt)
#                 visit[nxt][0] = visit[front][0] + 1
#                 visit[nxt][1] = visit[front][1]
#             # 같은 depth에 같은 숫자가 있었음
#             elif visit[nxt][0] == visit[front][0] + 1:
#                 visit[nxt][1] += visit[front][1]
#
#         if turn[0] == True and turn[1] == 0: break
#         elif turn[0] == True: turn[1] -= 1
#     if turn[0] == True and turn[1] == 0: break
#
# print(visit[k][0])
# print(visit[k][1])

# while len(q) != 0:
#     size = len(q)
#     for i in range(size):
#         front = q.pop(0)
#         if front == k:
#             method += 1
#             found = True
#         # front +1/-1/*2 가 방문한 적이 있는지 판단 후 있다면
#         # queue에 추가 후
#         # 찾고자하는 동생의 위치 k가 아닐 시 visit=True 변경 : 안그럼 복수개의 답을 못찾음
#         if front + 1 <= MAX and not visit[front + 1]:
#             q.append(front + 1)
#             if front + 1 != k: visit[front + 1] = True
#         if 0 <= front - 1 and not visit[front - 1]:
#             q.append(front - 1)
#             if front - 1 != k: visit[front - 1] = True
#         if front * 2 <= MAX and not visit[front * 2]:
#             q.append(front * 2)
#             if front * 2 != k: visit[front * 2] = True
#     if found: break
#     depth += 1
#     print(depth)

# # 1394 암호 : 수학..
# import math
# mod = 900528
# str = str(input())
# pwd = input()
# lenstr = len(str)
# lenpwd = len(pwd)
#
# loc = [] # pwd의 각 문자가 str의 몇번째에 있는지
# for c in pwd:
#     loc.append(str.find(c))
#
# answer = 0
# for i in range(1, lenpwd):
#     answer = (answer + math.pow(lenstr, i)) % mod
#
# for i in range(len(loc)):
#     answer = (answer + loc[i] * math.pow(lenstr, lenpwd-i-1)) % mod
#
# print(int(answer+1) % mod)

# # 1501 영어 읽기
# import sys
# from collections import defaultdict
# dict = defaultdict(int)
#
# n = int(input())
# for _ in range(n):
#     s1 = input()
#     if len(s1)==1 or len(s1)==2 or len(s1)==3:
#         dict[s1] += 1
#     else:
#         tmp = s1[0]+s1[-1]+''.join(sorted(s1[1:-1]))
#         dict[tmp] += 1 # key: 맨앞+맨뒤+중간sort, value: cnt
#
# m = int(input())
# for _ in range(m):
#     s2 = list(map(str, sys.stdin.readline().split()))
#     answer = 1
#     for ss in s2:
#         if len(ss)==1 or len(ss)==2 or len(ss)==3: tmp = ss
#         else: tmp = ss[0] + ss[-1] + ''.join(sorted(ss[1:-1]))
#         if tmp in dict: answer *= dict[tmp]
#     print(answer)

# # 9019 DSLR
# from collections import defaultdict
# def dslr(str, n):
#     if str == 'D':
#         return (2 * n) % 10000
#     elif str == 'S':
#         return n - 1 if n != 0 else 9999
#     elif str == 'L':
#         tmp = int(n / 1000)
#         return (n * 10) % 10000 + tmp
#     elif str == 'R':
#         tmp = n % 10
#         return tmp * 1000 + int(n / 10)
#
# t = int(input())
# for _ in range(t):
#     a, b = map(int, input().split())
#     q = []
#     q.append(a)
#     dct = defaultdict(int)
#     dct[a] = ""
#     while q:
#         tmp = q.pop(0)
#         if tmp == b:
#             print(dct[tmp])
#             break
#         for w in ['D', 'S', 'L', 'R']:
#             new = dslr(w, tmp)
#             if dct[new] == 0:
#                 q.append(new)
#                 dct[new] = dct[tmp] + w

# # 13549 숨바꼭질 3
# from collections import deque
# MAX = 100_001
# n, k = map(int, input().split())
# q = deque()
# q.append(n)
# visited = [-1 for _ in range(MAX)]
# visited[n] = 0
#
# while q:
#     tmp = q.popleft()
#     if tmp == k:
#         print(visited[tmp])
#         break
#     if 0 <= tmp - 1 < 100001 and visited[tmp - 1] == -1:
#         visited[tmp - 1] = visited[tmp] + 1
#         q.append(tmp - 1)
#     if 0 < tmp * 2 < 100001 and visited[tmp * 2] == -1:
#         visited[tmp * 2] = visited[tmp]
#         q.appendleft(tmp * 2)
#     if 0 <= tmp + 1 < 100001 and visited[tmp + 1] == -1:
#         visited[tmp + 1] = visited[tmp] + 1
#         q.append(tmp + 1)

# # 2447 별 찍기 - 10
# def recursion(t, row, col):
#     for i in range(3):
#         for j in range(3):
#             if i==1 and j==1:
#                 continue
#             elif t==3:
#                 star[row+i][col+j] = '*'
#             else:
#                 recursion(t//3, row+i*t//3, col+j*t//3)
#
# n = int(input())
# star = [[' ' for _ in range(n)] for _ in range(n)]
#
# recursion(n, 0, 0)
#
# for i in range(n):
#     for j in range(n):
#         print(star[i][j], end='')
#     print()

# # 25682 체스판 다시 칠하기 2
# import sys
#
# n, m, k = map(int, sys.stdin.readline().split())
# chessboard = []
# for i in range(n):
#     str = list(sys.stdin.readline().rstrip())
#     chessboard.append(str)
#
# def minPaint(color):
#     accsum = [[0] * (m+1) for _ in range(n+1)]
#     for i in range(n):
#         for j in range(m):
#             # 행+열 값이 짝수면 [0][0]과 색이 달라야함, 홀수면 [0][0]과 색이 같아야함
#             if (i+j)%2 == 0:
#                 value = chessboard[i][j] != color
#             else:
#                 value = chessboard[i][j] == color
#             # 누적합 구하는 식
#             accsum[i+1][j+1] = accsum[i][j+1]+accsum[i+1][j]-accsum[i][j]+value
#     cnt = sys.maxsize
#     for i in range(1, n-k+2):
#         for j in range(1, m-k+2):
#             # 2차원 배열 누적합 점화식, k 값
#             cnt = min(cnt, accsum[i+k-1][j+k-1]-accsum[i+k-1][j-1]-accsum[i-1][j+k-1]+accsum[i-1][j-1])
#     return cnt
#
# # 두 체스판 유형 중 더 낮은 값 선택
# print(min(minPaint('B'), minPaint('W')))


# # 9251 LCS : Longest Common Subsequence, 최장 공통 부분 수열
# import sys
# line1 = sys.stdin.readline()
# line2 = sys.stdin.readline()
# len1 = len(line1)-1
# len2 = len(line2)-1
#
# dp = [[0] * (len2+1) for _ in range(len1+1)]
#
# for i in range(1, len1 + 1):
#     for j in range(1, len2 + 1):
#         if line1[i-1] == line2[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#
# print(dp[len1][len2])
#



# # 5430 AC
# import sys
# from collections import deque
# T = int(sys.stdin.readline())
# while(T):
#     T-=1
#     # input
#     func = deque(sys.stdin.readline().strip())          # first line
#     num = int(sys.stdin.readline())                     # second line
#     tmp = sys.stdin.readline().strip().replace('[', '').replace(']', '')
#     if tmp == "": arr = []
#     else: arr = deque(map(int, tmp.split(',')))         # third line
#
#     # execute
#     err = False
#     seq = 1
#     s, e = 0, len(arr)-1
#     while(func):
#         if func[0] == 'R':
#             seq *= -1
#             func.popleft()
#         elif func[0] == 'D' and (s > e or len(arr) == 0):
#             err = True
#             break
#         elif func[0] == 'D':
#             if seq == 1: s += 1
#             else: e -= 1
#             func.popleft()
#
#     if err:
#         print("error")
#     elif seq == -1:
#         print("[", end='')
#         print(','.join(map(str, list(arr)[s:e+1][::-1])), end='')
#         print("]")
#     else:
#         print("[", end='')
#         print(','.join(map(str, list(arr)[s:e+1])), end='')
#         print("]")


# # 12865 평범한 배낭
# # 여행에 필요한 n개 물건, 각 물건은 무게 w와 가치 v
# # 물건을 넣어가면 v만큼 즐길 수 있음 / 최대 k만큼의 무게만을 넣을 수 있음
# # 배낭에 넣을 수 있는 물건들의 가치 최댓값을 출력해라
# #
# # 냅색 알고리즘 사용
# # m[i][w] : i개의 물건과 w무게 제한으로 만들 수 있는 최대 가치
# # m[0][w] = 0 for all w, m[i][0] = 0 for all i
# import sys
# # input
# n, k = map(int, sys.stdin.readline().split())
# stuff = []
# for _ in range(n):
#     w, v = map(int, sys.stdin.readline().split())
#     if w <= k: # 들 수 있는 최대 무게보다 가벼운 물건만
#         stuff.append([w, v])
#
# # 0/1 knapsack problem
# m = [[0 for i in range(k+1)] for i in range(n)]
# for i in range(n):
#     for j in range(k+1):
#         if stuff[i][0] >= j: # i번째 물건의 무게가 j보다 큰 경우, m[i-1][j]
#             m[i][j] = m[i-1][j]
#         else: # 다른 모든 경우
#             # max(무게가 같을 떄 이전 값(현재 물건 추가 안함), 현재 물건 포함해서 계산한 값)
#             m[i][j] = max(m[i-1][j], m[i-1][j-stuff[i][0]] + stuff[i][1])
#
# print(m[n-1][k])


# # 1068 트리
# N = int(input())
# node = list(map(int, input().split()))
# erase = int(input())
#
# def dfs(k):
#     node[k] = -2
#     for i in range(N):
#         if node[i] == k:
#             dfs(k)
#
# dfs(erase)
# cnt = 0
# for i in range(len(node)):
#     if node[i] != -2 and i not in node:
#         cnt += 1
# print(cnt)


# N = int(input())
# node = list(map(int, input().split()))
# erase = int(input())
#
# root = 0
# tree = [[] for _ in range(N)]
# for i in range(N):
#     if i == erase:
#         continue
#     if node[i] == -1:
#         root = i
#         continue
#     tree[node[i]].append(i)
#
# def dfs(n):
#     cnt = 1 if len(tree[n]) == 0 else 0
#     for leaf in tree[n]:
#         cnt += dfs(leaf)
#     return cnt
#
# if N==1: print(0)
# elif N==2: print(1)
# else: print(dfs(root))


# 1916 최소비용 구하기
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

S, E = map(int, input().split())

distance = [INF] * (N+1)
distance[S] = 0

def dijkstra():
    que = [(0, S)]
    while que:
        curW, cur = heapq.heappop(que)
        if distance[cur] < curW:    # 이미 처리되었으면 cont.
            continue
        for dest, w in graph[cur]:
            if distance[dest] > distance[cur] + w:
                distance[dest] = distance[cur] + w
                heapq.heappush(que, (cost, dest))

dijkstra()
print(distance[E])