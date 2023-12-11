# #10844 쉬운 계단 수: dynamic programming
# N = int(input())
# dp = [[0] * 10 for _ in range(N+1)]
# dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#
# for i in range(2, N+1):
#     dp[i][0] = dp[i-1][1]
#     dp[i][9] = dp[i-1][8]
#     for j in range(1, 9):
#         dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
#
# # N번째 행의 원소를 모두 더한 값이 계단 수의 개수
# print(sum(dp[N]) % 1000000000)

# # 1697 숨바꼭질
# # stop sign있으면 좋을 듯? 찾고 while문은 계속 돌아가지구... 또는 함수로 만들어서 찾았을때 리턴해버리던지..
# import sys
# MAX = 100000
# n, k = map(int, sys.stdin.readline().split())
# q = [n]
# visit = [False] * (MAX + 1)
# visit[n] = True
# depth = 0
#
# while len(q) != 0:
#     size = len(q)
#     for i in range(size):
#         front = q.pop(0)
#         if front == k:
#             print(depth)
#             break
#
#         if front + 1 <= MAX and not visit[front + 1]:
#             q.append(front + 1)
#             visit[front + 1] = True
#         if 0 <= front - 1 and not visit[front - 1]:
#             q.append(front - 1)
#             visit[front - 1] = True
#         if front * 2 <= MAX and not visit[front * 2]:
#             q.append(front * 2)
#             visit[front * 2] = True
#
#     depth += 1

# # 2504 괄호의 값
# bracket_str = input()
# stack = []
# ans = 0
# tmp = 1
# snd = False # 초반 ( 나올때 ans+=tmp안해주기 위해서..
# for c in bracket_str:
#     # c가 ) ] 이고, 앞에 짝이 맞으면 pop(), tmp값 update, else exit
#     if c==')' and stack[-1]=='(':
#         stack.pop()
#         tmp *= 2
#         snd = True
#     elif c==']' and stack[-1]=='[':
#         stack.pop()
#         tmp *= 3
#         snd = True
#     elif c==')' or c==']':
#         print("0")
#         exit()
#     # c가 ( [ 이면 append, ans값 update, tmp값 init
#     elif c=='(' or c=='[':
#         stack.append(c)
#         if snd:
#             ans += tmp
#             tmp = 1
#     else:
#         print("0")
#         exit()
# if tmp!=1: ans += tmp
# print(ans)

# # 13335 트럭
# n, w, L = map(int, input().split())
# # 트럭의 수 / 다리 길이 / 최대하중
# truck = list(map(int, input().split()))
# unit_time = 0
# bridge = []
# weight = 0
# idx = 0
# # 1반복=1time
# while idx < n:
#     # 차 빼기... 첫번쨰 차가 다리길이만큼 다 건너면..
#     if len(bridge)>0 and bridge[0][1] + w == unit_time:
#         weight -= bridge[0][0]
#         bridge.pop(0)
#
#     # 차 추가... 추가해도 최대하중 안넘고 다리길이가 안넘는다면..
#     if weight+truck[idx]<=L and len(bridge)<w:
#         tmp = []
#         tmp.append(truck[idx])
#         tmp.append(unit_time)
#
#         bridge.append(tmp)
#         weight += truck[idx]
#         idx += 1
#     unit_time += 1
# unit_time += w
# print(unit_time)

# # 2002 추월
# n = int(input())
# dg = []
# ys = dict()
# ans = 0
# # 들어가는 차
# for _ in range(n):
#     dg.append(input())
# # 나오는 차
# for i in range(n):
#     ys[input()] = i
#
# for i in range(n):
#     # 나오는 차순 != 들어가는 차순 이 가장 큰 값
#     j = ys[dg[i]]
#     if i != j and ans < abs(i - j):
#         ans = abs(i-j)
# print(ans)

# # 11403 경로 찾기
# n = int(input())
# g = [[0 for _ in range(n)] for _ in range(n)]
# # input
# for i in range(n):
#     a = list(map(int, input().split()))
#     for j in range(n):
#         g[i][j] = a[j]
# # floyd-Warshall
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             if g[j][k] == 0 and g[j][i] == 1 and g[i][k] == 1:
#                 g[j][k] = 1
# # print
# for i in range(n):
#     for j in range(n):
#         print(g[i][j], end=" ")
#     print()

# # 2583 영역 구하기
# xi = [-1, 1, 0, 0]
# yi = [0, 0, -1, 1]
# def DFS(i, j):
#     global cnt
#     if i < 0 or j < 0 or i >= m or j >= n:
#         return
#     elif paper[i][j] == 1:
#         return
#     elif paper[i][j] == 0:
#         cnt +=1
#         paper[i][j] = 1
#         for k in range(4):
#             DFS(i+xi[k], j+yi[k])
#     return
#
# m, n, k = map(int, input().split())
# paper = [[0 for _ in range(n)] for _ in range(m)]
# for row in range(k):
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(y1, y2):
#         for j in range(x1, x2):
#             paper[i][j] = 1
# # for i in range(m):
# #     print(paper[i])
# c = []
# for i in range(m):
#     for j in range(n):
#         if paper[i][j]==0:
#             cnt = 0
#             DFS(i, j)
#             c.append(cnt)
#             # print(i, j, c[-1])
# # print()
# # for i in range(m):
# #     print(paper[i])
#
#
# print(len(c))
# c.sort()
# for i in range(len(c)):
#     print(c[i], end=' ')

# num = int(input())
# nums = list(map(int, input().split()))
# oper = list(map(int, input().split()))
#
# maximum = -1e9
# minimum = 1e9
#
# def dfs(dep, res, nums, plus, minus, mul, div):
#     global maximum, minimum
#     if dep == len(nums)-1:
#         maximum = max(maximum, res)
#         minimum = min(minimum, res)
#
#     if plus:
#         dfs(dep+1, res+nums[dep+1], nums, plus-1, minus, mul, div)
#     if minus:
#         dfs(dep+1, res-nums[dep+1], nums, plus, minus-1, mul, div)
#     if mul:
#         dfs(dep+1, res*nums[dep+1], nums, plus, minus, mul-1, div)
#     if div:
#         if res<0: dfs(dep+1, -(abs(res)//nums[dep+1]), nums, plus, minus, mul, div-1)
#         else: dfs(dep+1, res//nums[dep+1], nums, plus, minus, mul, div-1)
#
# dfs(0, nums[0], nums, oper[0], oper[1], oper[2], oper[3])
# print(maximum)
# print(minimum)

# # 11729 하노이 탑 이동 순서
# # 1 2 3
# def hanoi(n, a, b): # number, start, end
#     if n > 1: hanoi(n-1, a, 6-a-b)
#     print(a, b)
#     if n > 1: hanoi(n-1, 6-a-b, b)
#
# n = int(input())
# print(2**n-1)
# hanoi(n, 1, 3)

# # 1149 RRB거리
# n = int(input())
# cases = [[0 for _ in range(3)] for _ in range(n)]
# cases[0] = list(map(int, input().split()))
# for i in range(1, n):
#     r, g, b = map(int, input().split())
#     cases[i][0] = r + min(cases[i-1][1], cases[i-1][2])
#     cases[i][1] = g + min(cases[i-1][0], cases[i-1][2])
#     cases[i][2] = b + min(cases[i-1][0], cases[i-1][1])
# print(min(cases[n-1]))

# # 16139 인간-컴퓨터 상호작용
# import sys
# strl = sys.stdin.readline()
# q = int(sys.stdin.readline())
# arr = [[0 for _ in range(26)] for _ in range(len(strl))]
#
# arr[0][ord(strl[0])-97] = 1 # 첫글자 누적합
# for i in range(1, len(strl)-1): # 2 ~ 끝 누적합
#     for j in range(26):
#         arr[i][j] = arr[i-1][j]
#     arr[i][ord(strl[i])-97] += 1
#
# for _ in range(q):
#     a, b, c = list(sys.stdin.readline().split())
#     b, c = int(b), int(c)
#     if b == 0: # 0이면 c 부분 출력
#         print(arr[c][ord(a) - 97])
#     else: # 누적합이므로 c-(b-1) 출력
#         print(arr[c][ord(a)-97] - arr[b-1][ord(a)-97])

# # 11660 구간 합 구하기 5
# import sys
# n, m = map(int, sys.stdin.readline().split())
# arr = list()
# # n * n Table
# for _ in range(n):
#     arr.append(list(map(int, input().split())))
# # 누적합 table
# accsum = [[0 for _ in range(n+1)] for _ in range(n+1)] # padding을 만들어서 [-1]이 됬을 때 0으로 처리해주기
# for i in range(n):
#     for j in range(n):
#         accsum[i][j] = accsum[i][j-1] + accsum[i-1][j] - accsum[i-1][j-1] + arr[i][j]
# # m번 누적합 구하기
# for i in range(m):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     print(accsum[x2-1][y2-1] + accsum[x1-2][y1-2] - accsum[x2-1][y1-2] - accsum[x1-2][y2-1])

# # 1931 회의실 배정
# # greedy algorithm
# # 그리디를 써서 사용 회의의 최대 개수를 찾아야 하는데
# # 끝 회의시간 정렬을 쭉 하고
# # 가장 빨리 끝나는 회의를 먼저 선택하고,
# # 이전에 이미 선택한 끝나는 시간에 가능한 회의를 택하고. .. 이런식으로
# n = int(input())
# lst = []
# for _ in range(n):
#     start, end = map(int, input().split())
#     lst.append((start, end))
# lst.sort(key=lambda x: (x[1], x[0]))
# use = 1
# bef = lst[0][1]
# for i in range(1, n):
#     if lst[i][0] >= bef:
#         use += 1
#         bef = lst[i][1]
#
# print(use)

# # 1992 쿼드 트리
# import sys
# n = int(input())
# video = []
# for _ in range(n):
#     video.append(list(sys.stdin.readline().strip()))
#
# def divfour(row, col, m):
#     # 다 1인지 확인
#     zero, one = True, True
#     for i in range(row, row+m):
#         for j in range(col, col+m):
#             if video[i][j] == '0':
#                 one = False
#             if video[i][j] == '1':
#                 zero = False
#     # print(row, col, m, zero, one)
#     # 섞임
#     if (zero or one) == False:
#         print("(", end='')
#         divfour(row, col, m // 2)
#         divfour(row, col+m//2, m // 2)
#         divfour(row+m//2, col, m // 2)
#         divfour(row+m//2, col+m//2, m // 2)
#         print(")", end='')
#     # 다 0
#     elif zero == True:
#         print(0, end='')
#     # 다 1
#     else:
#         print(1, end='')
#
# r, c, m = 0, 0, n
# divfour(r, c, m)

# # 1629 곱셈
# # 자연수 A를 B번 곱한 수를 알고 싶다.
# # 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하라
# #
# # (a*b)%c = a%c * b%c
# # a = 3, b = 11, c = 12
# # 3^11 % 12
# # = (3^5 * 3^5 * 3) % 12
# # = ((3^2 % 12 * 3^2%12 * 3) % 12 * (3^2 % 12 * 3^2%12 * 3) % 12 * 3) % 12
# import sys
# a, b, c = map(int, sys.stdin.readline().strip().split())
#
# def multi(a, n):
#     if n == 1:
#         return a%c
#     else:
#         tmp = multi(a, n//2)
#         if n%2 == 0:
#             return (tmp*tmp)%c
#         else:
#             return (tmp*tmp*a)%c
# print(multi(a, b))

# # 2156 포도주 시식
# grape = []
# n = int(input())
# for i in range(n):
#     grape.append(int(input()))
# dp = [0] * n
# if n > 0:
#     dp[0] = grape[0]
# if n > 1:
#     dp[1] = grape[0]+grape[1]
# if n > 2:
#     dp[2] = max(grape[0]+grape[2], grape[1]+grape[2], dp[1])
# for i in range(3, n):
#     # MAX( O X O , O X O O , O X )
#     dp[i] = max(grape[i]+dp[i-2], dp[i-3]+grape[i-1]+grape[i], dp[i-1])
# print(max(dp))

# # 1991 트리 순회
# tree = dict()
# n = int(input())
#
# for i in range(n):
#     node, left, right = map(str, input().strip().split())
#     if i == 0:
#         tree[1] = node
#         tree[node] = 1
#     cur = tree[node]
#     if left != '.':
#         tree[cur * 2] = left
#         tree[left] = cur * 2
#     if right != '.':
#         tree[cur * 2 + 1] = right
#         tree[right] = cur * 2 + 1
#
# def preorder(i):
#     if i in tree:
#         print(tree[i], end='')
#         preorder(i*2)
#         preorder(i*2+1)
#     else:
#         return
#
# def inorder(i):
#     if i in tree:
#         inorder(i*2)
#         print(tree[i], end='')
#         inorder(i*2+1)
#     else:
#         return
#
# def postorder(i):
#     if i in tree:
#         postorder(i*2)
#         postorder(i*2+1)
#         print(tree[i], end='')
#     else:
#         return
#
# preorder(1)
# print()
# inorder(1)
# print()
# postorder(1)



# # 1446 지름길
# import sys
# from collections import deque
#
# N, D = map(int, sys.stdin.readline().split())
# road = {0:{}, D:{}}
# for i in range(N):
#     a, b, c = map(int, sys.stdin.readline().split())
#     if not a in road:
#         road[a] = {}
#     if b > D: continue
#     elif not b in road[a] or road[a][b] > c: # 존재X or 기존 값보다 작을때 update
#         road[a][b] = c if c < b-a else b-a
#     if b <= D and not b in road:       # 도착 노드도 노드로 만들어줌
#         road[b] = {}
#
# # 노드 사이 길 생성(기본도로로 갈 경우)
# for x in road:
#     for y in road:
#         if x < y and y <= D and (not y in road[x] or road[x][y] > y-x) : #and road[x] == {}:
#             road[x][y] = y-x
#
# # dijkstra
#
# # 분기점(노드) 생성 -> 도로이기 때문에 무한이 아닌 본인 값을 넣어주었음
# distance = {0:0, D:D}
# for node in road:
#     distance[node] = node
#
# # 0에서 시작해서 지름길(road)로 빠르게 갈 수 있으면 업데이트 해줌
# que = deque()
# que.append(0)
#
# while que:
#     current = que.popleft()
#     cdist = distance[current]
#     for key, value in road[current].items():
#         # distance의 key까지의 저장된 거리
#         # 현재 노드에서 원래 길로 온 거리
#         # 보다 지름길을 선택하는 것이 더 짧다면 업데이트
#         distance[key] = min(distance[key],
#                             min(cdist + (key-current), cdist + value))
#         if not key in que:
#             que.append(key)
#
# print(distance[D])

# # 2343 기타 레슨
# import sys
# n, m = map(int, input().split())
# lect = list(map(int, input().split()))
# slect = [lect[0]]
# for i in range(1, n):
#     slect.append(slect[i-1]+lect[i])
#
# result = sys.maxsize
# left = max(lect)
# right = slect[-1]
# x = int((left+right)/2)
# while(left <= right):
#     s = 0
#     sum = 1
#     for i in range(n):
#         if slect[i] - (slect[s] if s != 0 else 0) > x:
#             s = i-1
#             sum += 1
#             if sum > m:
#                 left, right = x + 1, right
#                 break
#     if sum <= m:
#         result = min(result, x)
#         left, right = left, x - 1
#
#     x = int((left+right)/2)
# print(result)

# # 9934 완전 이진 트리
# k = int(input())
# order = list(map(int, input().split()))
# mktree = [[] for _ in range(k)]
#
# def dfs(tree, depth):
#     # 중간 부모 노드의 인덱스
#     mid = len(tree) // 2
#     # node 추가
#     mktree[depth].append(tree[mid])
#
#     if len(tree) == 1:
#         return
#
#     #
#     dfs(tree[:mid], depth+1)
#     dfs(tree[mid+1:], depth+1)
#
# dfs(order, 0)
# for i in mktree: print(*i)


# # 1105 팔
# import sys
# # 어떤 수 (n)에 들어있는 8의 개수를 구하는 함수
# def cnt8(n):
#     cnt = 0
#     while n:
#         if n%10==8: cnt+=1
#         n //= 10
#     return cnt
#
# # 범위 안에서 가장 8이 적은 수에 들어있는 8의 개수를 구하는 함수
# def findMininumCnt8(l, r):
#     res = sys.maxsize
#     for i in range(l, r + 1):
#         res = min(res, cnt8(i))
#     return res
#
# L, R = input().split()
#
# if len(L) != len(R):
#     print(0)
# else:
#     result, L, R = 0, int(L), int(R)
#     # 반복마다 1의 자리, 10의 자리...를 판별함
#     while R != 0 and L != 0:
#         if L == R:
#             result += cnt8(L)
#             break
#         result += findMininumCnt8(L%10, R%10 if L%10<R%10 else 10+R%10)
#         L, R = L//10, R//10
#     print(result)

# # 1660 캡틴 이다솜
# import sys
# n = int(input())
# deapo = [1,4,10,20]
#
# cnt, last = 5, 10
# while deapo[-1] <= n:
#     deapo.append(deapo[cnt-2]+cnt+last)
#     last += cnt
#     cnt += 1
#
# dp = [sys.maxsize for _ in range(n+1)]
# for i in range(1, n+1):
#     for num in deapo:
#         if num == i: # 같은 수라면 대포알을 다 쓰고 하나의 사면체로 만들 수 있음
#             dp[i] = 1
#         elif num <= i: # 대포알 사면체에 해당하는 수가 더 작다면 (이전+1)개로 만들 수 있음
#             dp[i] = min(dp[i], 1+dp[i-num])
#
# print(dp[n])



# # 1309 동물원
# # n=1 -> 3
# # n=2 -> 7
# # n=3 -> 17
# # n=4 -> 41
# # n=5 -> 99
# n = int(input())
# if n == 1:
#     print(3)
#     exit(0)
#
# cage = [0] * n
# cage[0], cage[1] = 3, 7
#
# for i in range(2, n):
#     cage[i] = (cage[i-1] * 2 + cage[i-2]) % 9901
# print(cage[n-1])

# testcase = int(input())
# for _ in range(testcase):
#     a, b = map(int,input().split())
#     last = a
#     if a == 1:
#         print(1)
#         exit(0)
#     for _ in range(b-1):
#         last = (last * a) % 10
#     print(last if last != 0 else 10)

testcase = int(input())
for _ in range(testcase):
    a, b = map(int,input().split())
    last = a % 10
    if last == 0:
        print(10)
    elif last in [1,5,6]:
        print(last)
    elif last in [4,9]:
        if b%2 == 0:
            print(last*last%10)
        else:
            print(last)
    else:
        if b%4 == 0:
            print(last**4%10)
        else:
            print(last**(b%4)%10)

# 0 > 0
# 1 > 1
# 2 > 2 4 8 6 ..
# 3 > 3 9 7 1 ..
# 4 > 4 6 ..
# 5 > 5
# 6 > 6
# 7 > 7 9 3 1 ..
# 8 > 8 4 2 6 ..
# 9 > 9 1 ..